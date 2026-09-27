# Case 05 — JPY 2022–2024: rate divergence, carry và intervention

Case này không phải câu chuyện đơn giản rằng “Fed tăng lãi suất nên USD/JPY tăng” hoặc “Nhật Bản can thiệp nên JPY chắc chắn đảo chiều”. Điều cần học là cách **monetary-policy divergence, carry positioning, import-cost shock, official intervention và market expectations** tương tác trong một currency pair lớn nhưng vẫn có thể trải qua gap, repricing và crowded positioning.

```text
Policy divergence
→ expected rate differential
→ forward points / carry incentive
→ capital flows and positioning
→ USD/JPY repricing
→ import-price and distributional effects
→ intervention expectation
→ liquidity / option-risk repricing
→ policy and balance-sheet response
```

`as_of_date: 2026-09-27`
Các số liệu can thiệp trong case là historical facts lấy từ nguồn chính thức; các scenario và trade ledger là simulation.

## 1. Regime trước cú sốc

Năm 2022, thị trường theo dõi một chênh lệch chính sách nổi bật: Federal Reserve chuyển sang thắt chặt nhanh trong khi Bank of Japan vẫn duy trì stance nới lỏng và kiểm soát đường cong lợi suất. Trong biên bản tháng 9/2022, BOJ ghi nhận thị trường quy một phần đà giảm của JPY cho khác biệt hướng đi chính sách giữa Nhật Bản và các nền kinh tế khác.

Điều này không tạo ra một công thức định giá duy nhất. Nó tạo ra một **state variable** mà market participants dùng để cập nhật:

```text
US front-end yields rise
+ expected BoJ normalization remains slow
→ USD/JPY forward carry becomes more attractive to hold
→ demand for USD against JPY can increase
```

Nhưng spot còn chịu:

```text
global risk sentiment
energy-import bill
Japanese trade/income flows
repatriation and hedging by Japanese investors
US yield volatility
official communication
```

Không được coi carry là free return. Carry position có thể bị đảo chiều khi spot jump, rate path đổi, margin tăng hoặc liquidity co lại.

## 2. Vì sao rate differential truyền vào spot nhưng không quyết định toàn bộ spot?

Trong simplified covered-interest-parity framing:

```text
forward USD/JPY
≈ spot USD/JPY × exp((r_USD − r_JPY) × T)
```

Chênh lệch lãi suất ảnh hưởng forward points và incentive hedge/fund. Nó không nói rằng spot phải tăng đều với một tốc độ cố định. Spot còn là giá clearing của:

```text
expected future rates
risk premium
balance-sheet capacity
terms of trade
positioning
option barriers
intervention probability
```

Một vị thế long USD/JPY có thể kiếm carry trong vài tuần rồi lỗ lớn trong một phiên nếu JPY safe-haven demand, policy repricing hoặc intervention làm thay đổi spot nhanh hơn carry tích lũy.

## 3. Import shock và distributional channel

JPY yếu làm giá hàng hóa nhập khẩu tính bằng JPY tăng, đặc biệt khi giá commodity tính bằng USD cũng tăng. Tác động không đồng nhất:

```text
Importer / household
→ higher yen cost for energy and food

Exporter with foreign revenue
→ higher yen value of foreign receipts

Firm with unhedged USD payable
→ margin pressure

Investor holding foreign assets
→ local-asset return plus JPY translation effect
```

Vì vậy “JPY yếu tốt cho Nhật Bản” là một câu quá thô. Cần tách **foreign-currency revenue**, **foreign-currency cost**, hedge ratio, timing và pass-through vào giá trong nước.

## 4. Intervention là policy tool khác với monetary-policy pivot

Trong case này cần tách ba lớp:

```text
BOJ monetary policy
→ sets domestic monetary/financial conditions

MOF decision to intervene
→ official FX operation intended to influence disorderly/rapid moves

BOJ execution as fiscal agent
→ operational channel for the government's FX operation
```

Một cuộc can thiệp円買い thường được biểu diễn ở mức cơ học là:

```text
official sector sells USD assets
→ buys JPY
→ immediate demand for JPY rises
```

Nhưng điều đó không tự động xóa:

```text
US–Japan expected rate differential
carry incentive
commodity/import shock
private-sector hedging demand
```

MOF cho biết thống kê can thiệp được công bố theo tổng số hàng tháng và chi tiết theo ngày ở chu kỳ quý. Do đó, một chart spot hoặc reserve change đơn lẻ không đủ để suy ra timing, size và mục tiêu của operation.

## 5. Mốc policy và intervention cần đọc

### 2022 — divergence và communication risk

BOJ tiếp tục nhấn mạnh mục tiêu ổn định giá và điều kiện trong nước, trong khi thị trường tập trung vào chênh lệch chính sách với Mỹ. Bộ Tài chính Nhật Bản xác nhận sau operation ngày 22/09/2022 rằng intervention được dùng trong bối cảnh biến động quá mức và tiếp tục theo dõi các chuyển động disorderly.

Bài học không phải “intervention thắng hay thua” trong một ngày. Câu hỏi đúng là:

```text
Operation có thay đổi expected policy path không?
Có làm giảm tốc độ/độ một chiều của move không?
Positioning có giảm hay chỉ chuyển sang option/barrier khác?
Private flow có hấp thụ operation sau đó không?
```

### 2024 — intervention lớn trong một regime khác

Sang 2024, BOJ review lại giai đoạn JPY suy yếu mạnh từ 2022 và ghi nhận widening interest-rate differentials là một yếu tố thị trường chú ý. BOJ review cũng ghi nhận JPY chạm vùng khoảng `160 JPY/USD` trong năm 2024.

MOF công bố các operation yen-buying trong quý II/2024 với tổng `¥9,788.5 billion` (29/04 và 01/05), và trong quý III/2024 với tổng `¥5,534.8 billion` (11–12/07). Các con số này là **reported intervention amounts**, không phải lợi nhuận/lỗ của nhà đầu tư và cũng không phải bằng chứng rằng mọi chuyển động spot sau đó do intervention gây ra.

## 6. Positioning và option market

Khi một chiều carry trở nên phổ biến, rủi ro không chỉ nằm ở spot direction:

```text
long USD/JPY cash or forward
→ positive carry under assumed path
→ short JPY convexity may emerge through options/barriers
→ stop clusters and dealer hedging can amplify a move
```

Ngay cả khi intervention được dự đoán, timing không chắc chắn. Trader có thể đối mặt với:

```text
gap through stop
wide bid/ask around announcement
forward-point repricing
option implied-volatility jump
cross-currency basis movement
margin call before thesis review
```

Vì thế, “intervention risk” phải được ghi như một **state-dependent jump risk**, không phải một mức support cụ thể trên chart.

## 7. Causal map của case

```text
Fed tightening + BoJ easing/YCC stance
→ US–Japan expected rate differential widens
→ USD/JPY carry appeal and long-USD positioning rise
→ JPY import-cost pressure and political sensitivity increase
→ MOF communication / intervention expectation rises
→ intervention may produce sharp spot move and volatility repricing
→ if rate differential and private flows remain, pressure can reappear
→ if policy path or risk regime changes, carry unwind can dominate
```

Map này có hai feedback loop:

```text
Loop A — trend/carry:
spot USD/JPY rises → mark-to-market reinforces long positioning → further demand

Loop B — intervention/unwind:
intervention signal → volatility and margin rise → positions reduce → JPY strengthens
```

Hai loop có thể chạy ngược chiều trong cùng một tuần. Không nên fit một causal story duy nhất sau khi chỉ nhìn chart.

## 8. Balance-sheet cases

### Case A — Japanese importer

Một importer phải thanh toán USD sau 90 ngày. Khi USD/JPY tăng:

```text
unhedged payable cost in JPY rises
forward hedge may protect budget rate
option hedge preserves upside but pays premium
```

Đánh giá hedge bằng **JPY cost variance + premium/carry + residual timing risk**, không bằng standalone derivative P/L.

### Case B — Japanese exporter

Exporter nhận USD sau 90 ngày. JPY yếu có thể làm doanh thu quy đổi tăng, nhưng hedge forward có thể khóa tỷ giá và bỏ lỡ upside. Nếu forecast volume không chắc chắn:

```text
over-hedge risk
delivery-date mismatch
natural hedge from USD costs
```

phải được ghi rõ.

### Case C — leveraged carry portfolio

Portfolio long USD/JPY, short-vol hoặc dùng margin có thể có daily carry dương nhưng vẫn chịu:

```text
gap loss
liquidation before rehedge
correlation change with equities/rates
option barrier trigger
```

Net P/L phải tách spot, forward points, funding, slippage, margin và hedge adjustment.

## 9. What this case does not prove

Case này **không chứng minh**:

```text
rate differential luôn dự báo đúng spot
intervention luôn đảo chiều trend
JPY luôn là safe-haven trong mọi risk-off episode
carry strategy có expected profit trong mọi sample
reported intervention amount bằng với private order-flow impact
```

Điều case chứng minh là cơ chế phải được conditional hóa theo regime, funding, positioning và execution.

## 10. Research exercise

Tạo một event-study table cho từng ngày có communication hoặc operation:

```text
event timestamp
policy state trước event
US 2Y / Japan 2Y hoặc proxy rate differential
USD/JPY spot và forward points
1-week / 1-month implied volatility nếu có
option risk reversal nếu có
reported intervention amount
first reaction
24h follow-through
5-day follow-through
positioning proxy
alternative explanations
```

Sau đó phân loại event vào một trong bốn nhóm:

```text
rate-path repricing
liquidity/intervention shock
risk-off carry unwind
commodity/import-flow shock
```

Không được gán causal effect chỉ vì spot đổi hướng sau headline. Ghi rõ data nào là contemporaneous, data nào chỉ được công bố sau đó.

## 11. Risk checklist

```text
[ ] Tách BOJ monetary policy khỏi MOF FX intervention
[ ] Tách forward carry khỏi expected spot return
[ ] Có currency exposure của importer/exporter cụ thể chưa?
[ ] Có gap, spread và margin assumption chưa?
[ ] Có option/barrier/positioning channel chưa?
[ ] Có timestamp và publication lag của intervention data chưa?
[ ] Có alternative explanation ngoài headline chưa?
[ ] Không dùng reserve change như intervention amount trực tiếp
[ ] Không biến intervention thành automatic reversal signal
[ ] Đánh giá hedge bằng combined exposure và residual risk
```

## 12. Sources

- [Bank of Japan — Summary of Opinions, September 21–22, 2022](https://www.boj.or.jp/en/mopo/mpmsche_minu/opinion_2022/opi220922.htm)
- [Bank of Japan — Review of Monetary Policy from a Broad Perspective, 2024](https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2024/k241219b.pdf)
- [Japan Ministry of Finance — September 26, 2022 press conference](https://www.mof.go.jp/public_relations/conference/my20220926.html)
- [Japan Ministry of Finance — Foreign Exchange Intervention Operations statistics](https://www.mof.go.jp/english/policy/international_policy/reference/feio/index.html)
- [Japan Ministry of Finance — April–June 2024 intervention operations](https://www.mof.go.jp/english/policy/international_policy/reference/feio/quarter/2024_2Qe.html)
- [Japan Ministry of Finance — July–September 2024 intervention operations](https://www.mof.go.jp/english/policy/international_policy/reference/feio/quarter/2024_3Qe.html)

Đọc cùng:

- [90_connections/01 — Intervention, reserves, REER and currency valuation](../90_connections/01_INTERVENTION_RESERVES_REER_AND_CURRENCY_VALUATION.md)
- [04 — Macro drivers, rates, carry and sessions](../04_MACRO_DRIVERS_RATES_CARRY_AND_SESSIONS.md)
- [11 — Portfolio FX risk](../11_PORTFOLIO_FX_RISK_CORRELATION_AND_FACTOR_EXPOSURE.md)
