# Forex Historical trường hợp (case / 사례) Studies

> **Mạch đọc:** Các trường hợp (case / 사례) đi từ regime/credibility đến funding, liquidity và chính sách (policy / 정책) phản hồi (response / 응답); đọc theo thứ tự để mỗi cú sốc mở rộng mô hình tư duy (mental model / 사고 모델) của trường hợp (case / 사례) trước, không học như bảy câu chuyện độc lập.

Các trường hợp (case / 사례) study này không dùng để học thuộc diễn biến lịch sử. Mục tiêu là luyện cách phân tích một cú sốc FX theo chuỗi:

```text
Policy Regime
→ Constraint
→ Market Expectations
→ Funding / Capital Flows
→ Positioning / Liquidity
→ Price Adjustment
→ Policy Response
→ Balance-Sheet Effects
→ Lessons for Risk Management
```

Mỗi trường hợp (case / 사례) phải trả lời bốn câu hỏi:

1. Trước cú sốc, cơ chế nào giữ tỷ giá hoặc funding hệ thống (system / 시스템) ổn định?
2. Điều kiện nào làm cơ chế đó mất credibility hoặc không còn đủ balance-sheet sức chứa (capacity / 용량)?
3. Khi regime gãy, price move và liquidity phản ứng như thế nào?
4. Bài học nào có thể generalize, và bài học nào chỉ đúng trong institutional setting của thời kỳ đó?

## Thứ tự đọc khuyến nghị

Tệp (file / 파일) number là stable identifier, còn chuỗi (sequence / 시퀀스) dưới đây đi theo chronology và phụ thuộc (dependency / 의존성) của cơ chế (mechanism / 메커니즘):

1. [01_ERM_1992_STERLING_CRISIS.md](./01_ERM_1992_STERLING_CRISIS.md) — fixed/semi-fixed exchange-rate commitment, chính sách (policy / 정책) credibility và xung đột (conflict / 충돌) giữa domestic cycle với bên ngoài (external / 외부) anchor.
2. [02_ASIAN_FINANCIAL_CRISIS_1997.md](./02_ASIAN_FINANCIAL_CRISIS_1997.md) — currency mismatch, short-term foreign funding, banking fragility, reserve pressure và sudden stop.
3. [06_KOREA_USD_FUNDING_STRESS_2008.md](./06_KOREA_USD_FUNDING_STRESS_2008.md) — exporter forward hedges, foreign-bank-branch rollover, basis stress và USD liquidity backstop.
4. [03_SNB_CHF_FLOOR_REMOVAL_2015.md](./03_SNB_CHF_FLOOR_REMOVAL_2015.md) — central-bank floor, balance-sheet commitment, gap rủi ro (risk / 위험) và broker/counterparty thất bại (failure / 실패).
5. [04_GLOBAL_USD_FUNDING_STRESS_2020.md](./04_GLOBAL_USD_FUNDING_STRESS_2020.md) — offshore dollar demand, cross-currency funding stress, swap lines và toàn cục (global / 전역) dollar plumbing.
6. [07_VIETNAM_FX_MANAGEMENT_STRESS_2022_2023.md](./07_VIETNAM_FX_MANAGEMENT_STRESS_2022_2023.md) — managed flexibility, reserve drawdown, band widening và chính sách (policy / 정책) sự đánh đổi (trade-off / 트레이드오프).
7. [05_JPY_RATE_DIVERGENCE_AND_INTERVENTION_2022_2024.md](./05_JPY_RATE_DIVERGENCE_AND_INTERVENTION_2022_2024.md) — chính sách (policy / 정책) divergence, carry positioning, import-cost shock, intervention và liquidity repricing.

## Bản đồ cơ chế xuyên trường hợp (case / 사례)

| trường hợp (case / 사례) | Stability cơ chế (mechanism / 메커니즘) trước stress | dạng thất bại (failure mode / 실패 모드) chính | chính sách (policy / 정책) phản hồi (response / 응답) cần phân biệt |
|---|---|---|---|
| ERM 1992 | exchange-rate band + tỷ lệ (rate / 비율)/intervention credibility | domestic cycle xung đột bên ngoài (external / 외부) anchor | tỷ lệ (rate / 비율) defense, intervention, regime exit |
| Asia 1997 | stable FX expectation + foreign funding | currency mismatch + sudden stop + banking vòng lặp (loop / 루프) | reserves, IMF program, restructuring |
| Korea 2008 | exporter forwards + offshore bank funding | USD rollover và maturity mismatch | reserve liquidity, Fed–BOK swap line |
| SNB 2015 | credible EUR/CHF floor | abrupt policy-boundary removal + price gap | floor abandonment, liquidity/counterparty phản hồi (response / 응답) |
| toàn cục (global / 전역) USD 2020 | normal offshore USD refinancing | dash for cash + collateral/funding shortage | central-bank swap lines and facilities |
| JPY 2022–2024 | accommodative Japan chính sách (policy / 정책) + liquid toàn cục (global / 전역) thị trường (market / 시장) | tỷ lệ (rate / 비율) divergence + carry crowding + intervention jump rủi ro (risk / 위험) | MOF intervention vs BOJ monetary chính sách (policy / 정책) |
| Vietnam 2022–2023 | managed flexibility + reserve/interbank khung phần mềm (framework / 프레임워크) | bên ngoài (external / 외부) tỷ lệ (rate / 비율) shock + reserve/liquidity ràng buộc (constraint / 제약조건) | intervention, tỷ lệ (rate / 비율) phản hồi (response / 응답), band widening |

Sau bảy trường hợp (case / 사례), hoàn thành [Lab 07 — Cross-Regime FX Stress Synthesis](../90_labs/07_CROSS_REGIME_FX_STRESS_SYNTHESIS_LAB.md). Lab buộc tách `vulnerability → trigger → amplifier → market failure → policy constraint`, tránh chọn một historical analog chỉ vì chart hoặc headline giống nhau.

## Cách đọc

Không biến trường hợp (case / 사례) thành câu chuyện kiểu “ai đúng/ai sai”. Hãy tách:

```text
Regime rule
Domestic macro state
External macro state
Balance-sheet exposure
FX funding structure
Policy tool
Market expectation
Liquidity condition
Trigger
Feedback loop
Exit from the regime
```

Sau mỗi trường hợp (case / 사례), viết một `mechanism map` và một `risk checklist` có thể áp dụng vào research hiện tại mà không giả định lịch sử sẽ lặp lại nguyên dạng.

## Liên kết

- [04 — Macro drivers, rates, carry and sessions](../04_MACRO_DRIVERS_RATES_CARRY_AND_SESSIONS.md)
- [05 — Execution, brokers, costs and risk](../05_EXECUTION_BROKERS_COSTS_AND_RISK.md)
- [10 — Backtesting and point-in-time FX data](../10_BACKTESTING_AND_POINT_IN_TIME_FX_DATA.md)
- [11 — Portfolio FX risk](../11_PORTFOLIO_FX_RISK_CORRELATION_AND_FACTOR_EXPOSURE.md)
- [13 — Advanced FX microstructure and order flow](../13_ADVANCED_FX_MICROSTRUCTURE_AND_ORDER_FLOW.md)
