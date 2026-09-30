# Trường hợp (case / 사례) 03 — SNB CHF Floor Removal 2015: chính sách (policy / 정책) floor, gap rủi ro (risk / 위험) và liquidity discontinuity

Ngày 15/01/2015, Swiss National Bank (SNB) chấm dứt minimum exchange tỷ lệ (rate / 비율) `CHF 1.20 per euro` mà ngân hàng đã duy trì từ 2011. Sự kiện này là trường hợp (case / 사례) kinh điển về **regime break, discontinuous price movement, stop-loss thất bại (failure / 실패) và broker/counterparty rủi ro (risk / 위험)**.

Điều cần học không phải “central bank luôn có thể đổi ý”. Điểm sâu hơn là: khi một chính sách (policy / 정책) commitment tạo artificial ranh giới (boundary / 경계) cho price trong thời gian dài, thị trường (market / 시장) cấu trúc (structure / 구조) và positioning có thể thích nghi quanh ranh giới (boundary / 경계) đó. Nếu commitment biến mất đột ngột, historical volatility và normal thực thi (execution / 실행) các giả định (assumptions / 가정들) có thể trở nên gần như vô nghĩa trong vài phút.

## 1. Vì sao SNB đặt floor?

Trong euro-area sovereign stress, Swiss franc chịu strong safe-haven demand.

CHF appreciation quá mạnh tạo lo ngại về:

```text
Deflation
Export competitiveness
Domestic economic activity
```

SNB thiết lập minimum exchange tỷ lệ (rate / 비율):

```text
EUR/CHF >= 1.20
```

và tuyên bố sẵn sàng mua foreign currency với quy mô lớn để enforce floor.

Mô hình tư duy (mental model / 사고 모델):

```text
Private demand for CHF
→ would push EUR/CHF lower
→ SNB creates CHF / buys foreign currency
→ absorbs pressure
→ keeps EUR/CHF near or above floor
```

## 2. Chính sách (policy / 정책) floor changes thị trường (market / 시장) phân phối (distribution / 분포)

Nếu thị trường (market / 시장) tin floor credible:

```text
EUR/CHF downside appears limited near 1.20
```

Điều này thay đổi hành vi (behavior / 동작) của traders và hedgers.

Strategies có thể bắt đầu dựa vào giả định (assumption / 가정):

```text
Below 1.20 is effectively unavailable
```

Nhưng chính sách (policy / 정책) ràng buộc (constraint / 제약조건) không phải vật lý (physical / 물리적) law.

## 3. Hidden option created by central bank

Một credible floor có payoff giống một implicit put-like chính sách (policy / 정책) hỗ trợ (support / 지원).

Participants gần floor có thể nghĩ:

```text
Downside limited by SNB
Upside remains open
```

Điều này có thể encourage crowded positioning.

Rủi ro (risk / 위험) bài toán (problem / 문제) xuất hiện nếu participants price chính sách (policy / 정책) commitment như certainty thay vì conditional regime.

## 4. Balance-sheet chi phí (cost / 비용) of maintaining floor

Để giữ floor khi CHF demand mạnh, SNB phải mua foreign assets.

Do đó central-bank balance sheet expands.

Chính sách (policy / 정책) sự đánh đổi (trade-off / 트레이드오프):

```text
Continue buying foreign currency
→ larger balance sheet / exposure

or
stop defending floor
→ CHF appreciates sharply
```

Không có costless option.

## 5. Euro-area chính sách (policy / 정책) matters

CHF floor không thể phân tích chỉ từ Switzerland.

Nếu ECB chính sách (policy / 정책) becomes more expansionary:

```text
EUR weakens
→ pressure on EUR/CHF floor increases
→ SNB must absorb more demand for CHF
```

Again, FX is relative macro.

## 6. December 2014: negative rates as hỗ trợ (support / 지원) công cụ (tool / 도구)

Trước khi bỏ floor, SNB announced negative interest tỷ lệ (rate / 비율) on sight deposits to reduce attractiveness of CHF holdings and hỗ trợ (support / 지원) minimum exchange tỷ lệ (rate / 비율).

Điều này cho thấy central bank có thể combine:

```text
FX intervention
+ interest-rate policy
```

Nhưng multiple tools không guarantee permanence of the regime.

## 7. January 15, 2015 chính sách (policy / 정책) break

SNB announced:

```text
Minimum exchange rate discontinued
Sight-deposit rate lowered to -0.75%
Three-month Libor target range lowered further
```

Đây là fundamental regime thay đổi (change / 변경), không phải normal dữ liệu (data / 데이터) surprise.

Before announcement:

```text
Market distribution conditioned on floor
```

After announcement:

```text
That boundary no longer exists
```

## 8. Why price moved discontinuously

Khi floor bị xóa:

```text
Existing buy/sell orders were not sufficient
at nearby prices
```

Thị trường (market / 시장) had to tìm kiếm (search / 검색) for a new clearing price.

Trong normal thị trường (market / 시장):

```text
1.2000
→ 1.1999
→ 1.1998
```

Trong regime break:

```text
large zones may have almost no executable liquidity
```

Price can jump through levels rather than trade smoothly through every điểm (point / 지점).

## 9. Stop-loss is an instruction, not a guaranteed price

Nếu trader long EUR/CHF near floor với stop below 1.20:

```text
Trigger condition occurs
→ stop becomes market order
→ no liquidity near expected stop
→ fill can occur far away
```

Planned mất mát (loss / 손실) and realized mất mát (loss / 손실) can diverge massively.

Lesson:

```text
Stop distance
is not maximum loss
when gap/liquidity discontinuity exists.
```

## 10. Leverage turns price gap into account insolvency

Suppose:

```text
Equity = 10,000
Notional exposure = 500,000
Effective leverage = 50x
```

A 1% adverse move implies roughly:

```text
5,000 loss
```

A much larger discontinuous move can exceed account equity before liquidation occurs.

Thus:

```text
Broker maximum leverage
+ assumed policy floor
= potentially catastrophic combination
```

## 11. Negative-balance rủi ro (risk / 위험)

In extreme gaps, a leveraged account can move from positive equity to negative before positions are closed.

Whether máy khách (client / 클라이언트) owes negative balance depends on:

```text
Jurisdiction
Product terms
Client classification
Broker policy / regulation
```

Never assume stop-out guarantees zero floor on equity.

## 12. Broker rủi ro (risk / 위험) becomes máy khách (client / 클라이언트) rủi ro (risk / 위험)

A broker/dealer aggregates many máy khách (client / 클라이언트) positions.

If many clients are positioned similarly:

```text
Market gaps
→ clients incur losses beyond deposits
→ broker has receivables from clients
→ broker may simultaneously owe liquidity providers
→ broker capital/liquidity stress rises
```

Thus thị trường (market / 시장) rủi ro (risk / 위험) can become counterparty rủi ro (risk / 위험).

## 13. Hedging is not instantaneous

A dealer may intend to hedge máy khách (client / 클라이언트) luồng (flow / 흐름) externally.

In discontinuous thị trường (market / 시장):

```text
hedge venue liquidity disappears
→ hedge price gaps
→ execution mismatch grows
```

A “fully hedged” nghiệp vụ (business / 비즈니스) mô hình (model / 모델) may still have basis, độ trễ (latency / 지연 시간) and gap exposure.

## 14. Why historical VaR fails near regime breaks

Suppose EUR/CHF spent years near floor with very low realized volatility.

Historical mô hình (model / 모델) learns:

```text
Daily move distribution is narrow
```

But observed phân phối (distribution / 분포) is conditional on chính sách (policy / 정책) regime.

Once regime changes:

```text
old sample no longer describes current process
```

This is **mô hình (model / 모델) regime rủi ro (risk / 위험)**.

## 15. Volatility suppression can hide tail rủi ro (risk / 위험)

Chính sách (policy / 정책) floor suppresses observed volatility on one side.

Therefore low realized volatility may reflect:

```text
Active policy intervention
```

not:

```text
Low latent economic pressure
```

This mirrors lesson from managed currencies in other crises.

## 16. Position sizing should include regime-gap scenario

Normal sizing:

```text
Allowed loss / stop distance
```

is incomplete for policy-bound instrument.

Need additional scenario:

```text
What if policy boundary disappears overnight?
```

Then kích thước (size / 크기) should consider:

```text
Gap to plausible stress price
Not only stop level
```

## 17. Chính sách (policy / 정책) credibility is not xác suất (probability / 확률) 100%

SNB had repeatedly emphasized commitment to floor before removing it.

Research lesson:

```text
Official commitment can be strong
without being literally permanent.
```

A trader should mô hình (model / 모델):

```text
Probability policy continues
Probability policy changes
Loss conditional on policy change
```

Expected mất mát (loss / 손실) may still be large even if policy-change xác suất (probability / 확률) seems small.

## 18. Asymmetric rủi ro (risk / 위험)

Near a defended floor, trade may look attractive:

```text
Small downside under regime
Potential upside if EUR rises
```

But true phân phối (distribution / 분포) includes:

```text
Rare regime-break state
with very large loss
```

This resembles short-volatility payoff:

```text
frequent small gains
+ rare catastrophic loss
```

## 19. Liquidity is trạng thái (state / 상태) dependent

A pair may be highly liquid in normal times.

Liquidity during regime break depends on willingness of thị trường (market / 시장) makers to quote into bất định (uncertainty / 불확실성).

```text
Normal liquidity
≠ stress liquidity
```

Rủi ro (risk / 위험) mô hình (model / 모델) must distinguish both.

## 20. Thị trường (market / 시장) thứ tự (order / 순서) vs limit thứ tự (order / 순서) sự đánh đổi (trade-off / 트레이드오프)

During gap:

### Thị trường (market / 시장) thứ tự (order / 순서)
Phần “Thị trường (market / 시장) thứ tự (order / 순서)” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


```text
Higher execution probability
Lower price certainty
```

### Limit thứ tự (order / 순서)
Phần “Limit thứ tự (order / 순서)” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


```text
Price protection
but may not execute
```

No thứ tự (order / 순서) kiểu (type / 타입) eliminates both price and thực thi (execution / 실행) rủi ro (risk / 위험).

## 21. Guaranteed stop is a separate sản phẩm (product / 제품) tính năng (feature / 기능)

If a broker explicitly offers guaranteed-stop protection under contractual terms, economics differ.

But ordinary stop thứ tự (order / 순서) is not guaranteed stop.

Always distinguish:

```text
Stop order
Guaranteed stop product
```

## 22. Rủi ro (risk / 위험) concentration across clients

A broker may appear diversified across thousands of clients.

But if clients all use same popular chiến lược (strategy / 전략) near chính sách (policy / 정책) floor:

```text
Client count high
but factor concentration also high
```

This is same portfolio lesson at broker mức (level / 수준).

## 23. Why backtest cannot reproduce this with ordinary candles

A daily candle only gives:

```text
Open
High
Low
Close
```

It does not tell:

```text
Executable bid/ask path
Depth
Rejected quotes
Latency
Actual fill availability
```

Therefore backtest around CHF 2015 needs high-resolution thị trường (market / 시장)/thực thi (execution / 실행) các giả định (assumptions / 가정들) and still contains bất định (uncertainty / 불확실성).

## 24. Options lesson

FX options incorporate xác suất (probability / 확률) phân phối (distribution / 분포) and jump rủi ro (risk / 위험) differently from spot.

Before regime break, option thị trường (market / 시장) may show:

```text
skew
implied volatility
barrier demand
```

that contains thông tin (information / 정보) about perceived tail rủi ro (risk / 위험).

But options are not perfect oracle; pricing also reflects supply/demand and chính sách (policy / 정책) credibility các giả định (assumptions / 가정들).

## 25. Central-bank balance sheet as regime variable

Research should monitor:

```text
FX reserves / foreign assets
Balance-sheet growth
Intervention pace
Domestic political debate
Inflation/deflation objective
External central-bank policy
```

Chính sách (policy / 정책) sustainability is động (dynamic / 동적).

## 26. What not to learn

Wrong lesson:

```text
"Never trust central banks."
```

Central-bank guidance often matters and many commitments persist.

Better lesson:

```text
Treat policy commitments as conditional regimes,
not physical guarantees.
```

Wrong lesson:

```text
"Use wider stop around central-bank events."
```

A wider stop still may be jumped.

Better lesson:

```text
Reduce exposure to survive discontinuity.
```

## 27. Stress-test template

For any policy-supported currency:

```text
Normal move: 1%
Large move: 5%
Regime break: 15–30%
Spread: 5x normal
No fill near stop
Margin requirement doubled
Counterparty unavailable for 30 minutes
```

Calculate:

```text
P/L
Equity
Margin level
Negative-balance risk
Counterparty dependency
```

## 28. Cơ chế (mechanism / 메커니즘) map
Phần “28. Cơ chế (mechanism / 메커니즘) map” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


```text
Safe-haven demand for CHF
→ SNB establishes EUR/CHF floor
→ intervention suppresses downside volatility
→ market adapts around credible boundary
→ balance-sheet/intervention burden grows
+ euro-area policy pressure
→ SNB removes floor
→ liquidity discontinuity
→ CHF reprices sharply
→ stop slippage / leveraged losses
→ client losses transmit to brokers/counterparties
```

## 29. Practical checklist derived from the trường hợp (case / 사례)

Before trading near chính sách (policy / 정책) ranh giới (boundary / 경계):

```text
What is exact policy commitment?
Is it legally/operationally guaranteed?
How is it enforced?
What would cause policy reversal?
How crowded is positioning?
What does option market imply?
What happens if no quotes exist near stop?
Can account survive 10x normal move?
Can broker survive client losses?
Is negative-balance protection contractual/regulatory?
```

## 30. Research exercise

Create a hypothetical EUR/CHF position before 15/01/2015:

```text
Equity = 50,000 CHF
Long EUR/CHF notional = 500,000 EUR
Entry = 1.2010
Stop = 1.1980
```

First calculate planned stop mất mát (loss / 손실) under normal thực thi (execution / 실행).

Then ignore stop and stress fill at:

```text
1.15
1.10
1.05
```

Compare:

```text
Planned loss
Stress loss
Equity remaining
Effective leverage after first move
```

Mục tiêu là thấy why stop-based rủi ro (risk / 위험) ngân sách (budget / 예산) fails under discontinuity.

## Nguồn nền
Phần “Nguồn nền” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


- Swiss National Bank, press bản phát hành (release / 릴리스), **15 January 2015 — SNB discontinues minimum exchange tỷ lệ (rate / 비율) and lowers interest tỷ lệ (rate / 비율) to -0.75%**.
- Swiss National Bank, monetary-policy chronology describing establishment and removal of the EUR/CHF minimum exchange tỷ lệ (rate / 비율).

Trường hợp (case / 사례) này tập trung vào mechanics of regime break, không dùng hindsight để khẳng định việc bỏ floor có thể được dự đoán chắc chắn.
