# Lab 06 — Vietnam FX-Management Stress

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Lab 06 — Vietnam FX-Management Stress**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. sản phẩm tạo ra (artifact / 산출물) đặc tả hợp đồng (contract / 계약)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. trường hợp (case / 사례) A — Regime map trước khi nhìn chart** để đem mô hình vào tình huống cụ thể. Mạch này nối FX management của Việt Nam với regime, liquidity, intervention và risk control, để lab phản ánh ràng buộc thực tế.

Lab này biến [Case 07 — Vietnam FX-management stress 2022–2023](../80_case_studies/07_VIETNAM_FX_MANAGEMENT_STRESS_2022_2023.md) thành một bài tập có thể kiểm tra (audit / 감사). Mục tiêu không phải dự báo USD/VND hay tìm một mức tỷ giá “đúng”, mà là phân biệt:

```text
regime rule
→ external shock
→ policy response
→ reserve / liquidity constraint
→ corporate cash-flow effect
→ hedge decision
→ observed result and residual risk
```

Mọi trường hợp (case / 사례) số dưới đây là simulation. Nếu thay bằng dữ liệu thật, ghi `as_of_date`, timestamp, nguồn (source / 소스), publication lag và market-access giả định (assumption / 가정).

## 1. sản phẩm tạo ra (artifact / 산출물) đặc tả hợp đồng (contract / 계약)

Tạo bốn đầu ra (output / 출력):

```text
vnd_regime_map.md
vnd_policy_tradeoff_table.md
vnd_importer_exporter_hedge_sheet.md
vnd_event_study_without_hindsight.md
```

Mỗi đầu ra (output / 출력) phải phân loại:

```text
Fact
Estimate
Assumption
Scenario
Decision Rule
Observed Result
Post-mortem
```

Không dùng một bank quote hiện tại để suy ra toàn bộ regime lịch sử. Không trộn tham chiếu (reference / 참조) tỷ lệ (rate / 비율), interbank quote, retail conversion tỷ lệ (rate / 비율) và executable hedge price trong cùng một cột.

> **Chuyển mạch:** Trong **Lab 06 — Vietnam FX-Management Stress**, **1. sản phẩm tạo ra (artifact / 산출물) đặc tả hợp đồng (contract / 계약)** cho ta quy tắc; **2. trường hợp (case / 사례) A — Regime map trước khi nhìn chart** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **3. trường hợp (case / 사례) B — Reserve drawdown decomposition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. trường hợp (case / 사례) A — Regime map trước khi nhìn chart

Giả sử bạn phải phân tích USD/VND trong một giai đoạn bên ngoài (external / 외부) USD shock. Điền bảng:

| tầng (layer / 계층) | Câu hỏi | đầu ra (output / 출력) bắt buộc |
|---|---|---|
| Regime | Tỷ giá được quản lý ở lớp nào? | tham chiếu (reference / 참조), band, interbank, authorized truy cập (access / 접근) |
| Instrument | Doanh nghiệp hedge bằng gì? | spot, forward, swap, option, natural hedge |
| luồng (flow / 흐름) | USD demand/supply đến từ đâu? | trade, debt dịch vụ (service / 서비스), FDI, portfolio, resident demand |
| chính sách (policy / 정책) | Công cụ nào có thể dùng? | tỷ lệ (rate / 비율), liquidity, intervention, band communication |
| ràng buộc (constraint / 제약조건) | Cái gì giới hạn chính sách (policy / 정책)? | reserves, inflation, growth, banking liquidity, capital truy cập (access / 접근) |
| thực thi (execution / 실행) | Quote nào thực sự executable? | bank, tenor, settlement, collateral, spread |

Sau đó viết nhân quả (causal / 인과적) map tối đa 12 nút (node / 노드). Map phải có ít nhất một nhánh đi ngược với kết luận ban đầu, ví dụ export receipts hỗ trợ USD supply trong khi imported-energy demand tăng USD demand.

> **Chuyển mạch:** Ở chặng này của **Lab 06 — Vietnam FX-Management Stress**, **2. trường hợp (case / 사례) A — Regime map trước khi nhìn chart** cho ta quy tắc; **3. trường hợp (case / 사례) B — Reserve drawdown decomposition** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **4. trường hợp (case / 사례) C — Policy-trade-off ma trận (matrix / 행렬)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. trường hợp (case / 사례) B — Reserve drawdown decomposition

Giả sử bảng reserve thay đổi như sau:

```text
Beginning reserves             = USD 100bn
Reported ending reserves       = USD 78bn
FX valuation effect            = −USD 4bn
Debt-service outflow           = −USD 6bn
Trade-flow / settlement effect = +USD 3bn
Other disclosed flow           = −USD 2bn
```

Tính phần **residual** và trình bày ba cách diễn giải:

```text
mechanical residual
possible intervention component
components that cannot be identified from aggregate data alone
```

Không được ghi “intervention = reserve decrease”. Một reserve series có thể chứa valuation, debt dịch vụ (service / 서비스), deposits, forward positions hoặc timing differences. Nếu không có transaction-level dữ liệu (data / 데이터), kết luận phải ghi là `not identified` hoặc `bounded estimate`.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Lab 06 — Vietnam FX-Management Stress**, **3. trường hợp (case / 사례) B — Reserve drawdown decomposition** cho ta quy tắc; **4. trường hợp (case / 사례) C — Policy-trade-off ma trận (matrix / 행렬)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **5. trường hợp (case / 사례) D — Band widening và thực thi (execution / 실행) stress** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. trường hợp (case / 사례) C — Policy-trade-off ma trận (matrix / 행렬)

Giả sử:

```text
Global USD index +6%
US 2Y yield +80 bp
Vietnam headline inflation +0.8 percentage point
Domestic credit growth slows
Importers report wider USD quote spread
Reserves are below the preferred buffer
```

So sánh bốn phản hồi (response / 응답):

```text
A. raise policy rates
B. add local-currency liquidity
C. use FX intervention
D. widen tolerated exchange-rate movement
```

Với mỗi phản hồi (response / 응답), điền:

```text
immediate FX effect
inflation effect
growth / credit effect
reserve effect
bank-liquidity effect
who bears the cost
what would falsify the thesis
```

Không chọn phản hồi (response / 응답) bằng một score tổng duy nhất. Nêu rõ mục tiêu (objective / 목표) hàm (function / 함수): giảm disorderly move, giữ inflation expectation, hỗ trợ growth hay bảo vệ reserve buffer.

> **Chuyển mạch:** Trong **Lab 06 — Vietnam FX-Management Stress**, **4. trường hợp (case / 사례) C — Policy-trade-off ma trận (matrix / 행렬)** cho ta quy tắc; **5. trường hợp (case / 사례) D — Band widening và thực thi (execution / 실행) stress** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **6. trường hợp (case / 사례) E — Importer versus exporter** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. trường hợp (case / 사례) D — Band widening và thực thi (execution / 실행) stress

Giả sử trước band widening:

```text
Reference rate = 24,000 VND/USD
Quoted bank band = ±3%
Importer payable = USD 5m, due in 90 days
```

Sau đó mô phỏng band `±5%` và ba quote conditions:

```text
Normal:    narrow spread, T+2 settlement
Stressed:  wide spread, reduced ticket size, delayed confirmation
Disorderly: quote interruption, partial fill, additional collateral
```

Tính phạm vi (range / 범위) tỷ giá theo band chỉ như **chính sách (policy / 정책) ranh giới (boundary / 경계) scenario**, không coi đó là guaranteed thực thi (execution / 실행). Lập bảng:

```text
budget rate
worst-case cash requirement
forward hedge notional
unhedged residual
spread / slippage assumption
settlement and collateral risk
```

> **Chuyển mạch:** Ở chặng này của **Lab 06 — Vietnam FX-Management Stress**, **5. trường hợp (case / 사례) D — Band widening và thực thi (execution / 실행) stress** cho ta quy tắc; **6. trường hợp (case / 사례) E — Importer versus exporter** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **7. trường hợp (case / 사례) F — sự kiện (event / 이벤트) study không hindsight** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. trường hợp (case / 사례) E — Importer versus exporter

### Importer

Một importer có `USD 10m` payable, nhưng amount thực tế có thể dao động `±20%` và date có thể trễ `30 ngày`.

So sánh:

```text
100% forward hedge
80% layered forward hedge
zero-cost collar / option structure
natural hedge from USD revenue
```

Đánh giá bằng:

```text
VND cash-flow variance
over-hedge loss when invoice falls
roll / timing cost
counterparty and collateral requirement
operational ability to settle
```

### Exporter

Một exporter dự kiến nhận `USD 8m`, nhưng có `USD 3m` đầu vào (input / 입력) chi phí (cost / 비용) tự nhiên. Tính exposure ròng trước khi chọn hedge ratio. Không hedge toàn bộ gross receivable như thể đầu vào (input / 입력) chi phí (cost / 비용) không tồn tại.

Stress:

```text
receivable delayed 45 days
USD/VND rises 4%
export volume falls 25%
local input costs rise 3%
```

Tách derivative P/L khỏi combined operating margin.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Lab 06 — Vietnam FX-Management Stress**, **6. trường hợp (case / 사례) E — Importer versus exporter** cho ta quy tắc; **7. trường hợp (case / 사례) F — sự kiện (event / 이벤트) study không hindsight** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **8. trường hợp (case / 사례) G — Cross-border investor return** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. trường hợp (case / 사례) F — sự kiện (event / 이벤트) study không hindsight

Chọn một giai đoạn có ít nhất ba sự kiện (event / 이벤트) timestamps. Với mỗi sự kiện (event / 이벤트), ghi snapshot trước khi sự kiện (event / 이벤트) xảy ra:

```text
USD broad index
US/Vietnam rate differential or proxy
USD/VND reference and bank quote
trading band
reserve observation available at that date
trade balance / export-import signal
bank liquidity proxy
policy expectation
```

Sau sự kiện (event / 이벤트), ghi:

```text
first reaction
1-day / 5-day / 20-day move
spread and liquidity change
policy follow-through
revision or later data release
```

Không dùng reserve dữ liệu (data / 데이터) công bố sau sự kiện (event / 이벤트) để viết pre-event thesis. Nếu timestamp không chắc, đánh dấu observation là unavailable.

> **Chuyển mạch:** Trong **Lab 06 — Vietnam FX-Management Stress**, **7. trường hợp (case / 사례) F — sự kiện (event / 이벤트) study không hindsight** cho ta quy tắc; **8. trường hợp (case / 사례) G — Cross-border investor return** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **9. Research-quality gates** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. trường hợp (case / 사례) G — Cross-border investor return

Một investor có:

```text
VND liability = 2bn VND
Vietnam equity fund = 1bn VND
USD asset      = USD 50,000
hedge          = none
```

Tính stress trong ba scenario:

```text
VND weakens 5%, local equity +8%
VND strengthens 5%, local equity −6%
VND flat, USD asset −10% in USD terms
```

Tách:

```text
local asset return
translation return
liability revaluation
conversion spread
wrapper / tax / settlement item to verify
```

Mục tiêu là thấy investor return phụ thuộc reporting currency và liability currency, không chỉ asset price.

> **Chuyển mạch:** Ở chặng này của **Lab 06 — Vietnam FX-Management Stress**, **8. trường hợp (case / 사례) G — Cross-border investor return** cho ta quy tắc; **9. Research-quality gates** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **10. Đọc tiếp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Research-quality gates

Bài chỉ đạt khi:

```text
[ ] regime được mô tả trước khi kết luận direction
[ ] reserve change không bị gán thẳng thành intervention
[ ] policy response có trade-off và constraint
[ ] reference/band/interbank/executable quote được tách
[ ] importer và exporter có exposure khác nhau
[ ] hedge ratio phản ánh amount/timing uncertainty
[ ] event study giữ publication lag
[ ] result được attribution thành spot, carry, cost và residual risk
[ ] không áp rule EUR/USD trực tiếp vào USD/VND
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Lab 06 — Vietnam FX-Management Stress**, **10. Đọc tiếp** tiếp nhận điểm tựa từ **9. Research-quality gates** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 10. Đọc tiếp

- [Case 07 — Vietnam FX-management stress 2022–2023](../80_case_studies/07_VIETNAM_FX_MANAGEMENT_STRESS_2022_2023.md)
- [15 — Korea / Vietnam FX market context and regulations](../15_KOREA_VIETNAM_FX_MARKET_CONTEXT_AND_REGULATIONS.md)
- [04 — Macro drivers, rates, carry and sessions](../04_MACRO_DRIVERS_RATES_CARRY_AND_SESSIONS.md)
- [11 — Portfolio FX risk](../11_PORTFOLIO_FX_RISK_CORRELATION_AND_FACTOR_EXPOSURE.md)

> **Bàn giao:** Sau **10. Đọc tiếp**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
