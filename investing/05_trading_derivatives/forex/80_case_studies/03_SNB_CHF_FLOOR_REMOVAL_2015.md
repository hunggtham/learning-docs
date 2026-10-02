# Trường hợp (case / 사례) 03 — SNB CHF Floor Removal 2015: chính sách (policy / 정책) floor, gap rủi ro (risk / 위험) và liquidity discontinuity

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Trường hợp (case / 사례) 03 — SNB CHF Floor Removal 2015: chính sách (policy / 정책) floor, gap rủi ro (risk / 위험) và liquidity discontinuity**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Vì sao SNB đặt floor?** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Chính sách (policy / 정책) floor changes thị trường (market / 시장) phân phối (distribution / 분포)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối SNB CHF floor removal với peg, reserve và shock transmission, để giải thích cú nhảy tỷ giá qua thay đổi cam kết chính sách.

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

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 03 — SNB CHF Floor Removal 2015: chính sách (policy / 정책) floor, gap rủi ro (risk / 위험) và liquidity discontinuity**, **2. Chính sách (policy / 정책) floor changes thị trường (market / 시장) phân phối (distribution / 분포)** tiếp nhận điểm tựa từ **1. Vì sao SNB đặt floor?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Hidden option created by central bank** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — SNB CHF Floor Removal 2015: chính sách (policy / 정책) floor, gap rủi ro (risk / 위험) và liquidity discontinuity**, **3. Hidden option created by central bank** tiếp nhận điểm tựa từ **2. Chính sách (policy / 정책) floor changes thị trường (market / 시장) phân phối (distribution / 분포)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Balance-sheet chi phí (cost / 비용) of maintaining floor** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Hidden option created by central bank

Một credible floor có payoff giống một implicit put-like chính sách (policy / 정책) hỗ trợ (support / 지원).

Participants gần floor có thể nghĩ:

```text
Downside limited by SNB
Upside remains open
```

Điều này có thể encourage crowded positioning.

Rủi ro (risk / 위험) bài toán (problem / 문제) xuất hiện nếu participants price chính sách (policy / 정책) commitment như certainty thay vì conditional regime.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — SNB CHF Floor Removal 2015: chính sách (policy / 정책) floor, gap rủi ro (risk / 위험) và liquidity discontinuity**, **4. Balance-sheet chi phí (cost / 비용) of maintaining floor** tiếp nhận điểm tựa từ **3. Hidden option created by central bank** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Euro-area chính sách (policy / 정책) matters** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 03 — SNB CHF Floor Removal 2015: chính sách (policy / 정책) floor, gap rủi ro (risk / 위험) và liquidity discontinuity**, **5. Euro-area chính sách (policy / 정책) matters** tiếp nhận điểm tựa từ **4. Balance-sheet chi phí (cost / 비용) of maintaining floor** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. December 2014: negative rates as hỗ trợ (support / 지원) công cụ (tool / 도구)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Euro-area chính sách (policy / 정책) matters

CHF floor không thể phân tích chỉ từ Switzerland.

Nếu ECB chính sách (policy / 정책) becomes more expansionary:

```text
EUR weakens
→ pressure on EUR/CHF floor increases
→ SNB must absorb more demand for CHF
```

Again, FX is relative macro.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — SNB CHF Floor Removal 2015: chính sách (policy / 정책) floor, gap rủi ro (risk / 위험) và liquidity discontinuity**, **6. December 2014: negative rates as hỗ trợ (support / 지원) công cụ (tool / 도구)** tiếp nhận điểm tựa từ **5. Euro-area chính sách (policy / 정책) matters** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. January 15, 2015 chính sách (policy / 정책) break** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. December 2014: negative rates as hỗ trợ (support / 지원) công cụ (tool / 도구)

Trước khi bỏ floor, SNB announced negative interest tỷ lệ (rate / 비율) on sight deposits to reduce attractiveness of CHF holdings and hỗ trợ (support / 지원) minimum exchange tỷ lệ (rate / 비율).

Điều này cho thấy central bank có thể combine:

```text
FX intervention
+ interest-rate policy
```

Nhưng multiple tools không guarantee permanence of the regime.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — SNB CHF Floor Removal 2015: chính sách (policy / 정책) floor, gap rủi ro (risk / 위험) và liquidity discontinuity**, **7. January 15, 2015 chính sách (policy / 정책) break** tiếp nhận điểm tựa từ **6. December 2014: negative rates as hỗ trợ (support / 지원) công cụ (tool / 도구)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Why price moved discontinuously** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 03 — SNB CHF Floor Removal 2015: chính sách (policy / 정책) floor, gap rủi ro (risk / 위험) và liquidity discontinuity**, **8. Why price moved discontinuously** tiếp nhận điểm tựa từ **7. January 15, 2015 chính sách (policy / 정책) break** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Stop-loss is an instruction, not a guaranteed price** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — SNB CHF Floor Removal 2015: chính sách (policy / 정책) floor, gap rủi ro (risk / 위험) và liquidity discontinuity**, **9. Stop-loss is an instruction, not a guaranteed price** tiếp nhận điểm tựa từ **8. Why price moved discontinuously** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Leverage turns price gap into account insolvency** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — SNB CHF Floor Removal 2015: chính sách (policy / 정책) floor, gap rủi ro (risk / 위험) và liquidity discontinuity**, **10. Leverage turns price gap into account insolvency** tiếp nhận điểm tựa từ **9. Stop-loss is an instruction, not a guaranteed price** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Negative-balance rủi ro (risk / 위험)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 03 — SNB CHF Floor Removal 2015: chính sách (policy / 정책) floor, gap rủi ro (risk / 위험) và liquidity discontinuity**, **11. Negative-balance rủi ro (risk / 위험)** tiếp nhận điểm tựa từ **10. Leverage turns price gap into account insolvency** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Broker rủi ro (risk / 위험) becomes máy khách (client / 클라이언트) rủi ro (risk / 위험)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — SNB CHF Floor Removal 2015: chính sách (policy / 정책) floor, gap rủi ro (risk / 위험) và liquidity discontinuity**, **12. Broker rủi ro (risk / 위험) becomes máy khách (client / 클라이언트) rủi ro (risk / 위험)** tiếp nhận điểm tựa từ **11. Negative-balance rủi ro (risk / 위험)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Hedging is not instantaneous** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — SNB CHF Floor Removal 2015: chính sách (policy / 정책) floor, gap rủi ro (risk / 위험) và liquidity discontinuity**, **13. Hedging is not instantaneous** tiếp nhận điểm tựa từ **12. Broker rủi ro (risk / 위험) becomes máy khách (client / 클라이언트) rủi ro (risk / 위험)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Why historical VaR fails near regime breaks** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Hedging is not instantaneous

A dealer may intend to hedge máy khách (client / 클라이언트) luồng (flow / 흐름) externally.

In discontinuous thị trường (market / 시장):

```text
hedge venue liquidity disappears
→ hedge price gaps
→ execution mismatch grows
```

A “fully hedged” nghiệp vụ (business / 비즈니스) mô hình (model / 모델) may still have basis, độ trễ (latency / 지연 시간) and gap exposure.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 03 — SNB CHF Floor Removal 2015: chính sách (policy / 정책) floor, gap rủi ro (risk / 위험) và liquidity discontinuity**, **14. Why historical VaR fails near regime breaks** tiếp nhận điểm tựa từ **13. Hedging is not instantaneous** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Volatility suppression can hide tail rủi ro (risk / 위험)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — SNB CHF Floor Removal 2015: chính sách (policy / 정책) floor, gap rủi ro (risk / 위험) và liquidity discontinuity**, **15. Volatility suppression can hide tail rủi ro (risk / 위험)** tiếp nhận điểm tựa từ **14. Why historical VaR fails near regime breaks** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Position sizing should include regime-gap scenario** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — SNB CHF Floor Removal 2015: chính sách (policy / 정책) floor, gap rủi ro (risk / 위험) và liquidity discontinuity**, **16. Position sizing should include regime-gap scenario** tiếp nhận điểm tựa từ **15. Volatility suppression can hide tail rủi ro (risk / 위험)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Chính sách (policy / 정책) credibility is not xác suất (probability / 확률) 100%** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 03 — SNB CHF Floor Removal 2015: chính sách (policy / 정책) floor, gap rủi ro (risk / 위험) và liquidity discontinuity**, **17. Chính sách (policy / 정책) credibility is not xác suất (probability / 확률) 100%** tiếp nhận điểm tựa từ **16. Position sizing should include regime-gap scenario** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Asymmetric rủi ro (risk / 위험)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — SNB CHF Floor Removal 2015: chính sách (policy / 정책) floor, gap rủi ro (risk / 위험) và liquidity discontinuity**, **18. Asymmetric rủi ro (risk / 위험)** tiếp nhận điểm tựa từ **17. Chính sách (policy / 정책) credibility is not xác suất (probability / 확률) 100%** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Liquidity is trạng thái (state / 상태) dependent** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — SNB CHF Floor Removal 2015: chính sách (policy / 정책) floor, gap rủi ro (risk / 위험) và liquidity discontinuity**, **19. Liquidity is trạng thái (state / 상태) dependent** tiếp nhận điểm tựa từ **18. Asymmetric rủi ro (risk / 위험)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Thị trường (market / 시장) thứ tự (order / 순서) vs limit thứ tự (order / 순서) sự đánh đổi (trade-off / 트레이드오프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Liquidity is trạng thái (state / 상태) dependent

A pair may be highly liquid in normal times.

Liquidity during regime break depends on willingness of thị trường (market / 시장) makers to quote into bất định (uncertainty / 불확실성).

```text
Normal liquidity
≠ stress liquidity
```

Rủi ro (risk / 위험) mô hình (model / 모델) must distinguish both.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 03 — SNB CHF Floor Removal 2015: chính sách (policy / 정책) floor, gap rủi ro (risk / 위험) và liquidity discontinuity**, **19. Liquidity is trạng thái (state / 상태) dependent** đã nêu tiêu chí phân biệt, còn **20. Thị trường (market / 시장) thứ tự (order / 순서) vs limit thứ tự (order / 순서) sự đánh đổi (trade-off / 트레이드오프)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **21. Guaranteed stop is a separate sản phẩm (product / 제품) tính năng (feature / 기능)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Thị trường (market / 시장) thứ tự (order / 순서) vs limit thứ tự (order / 순서) sự đánh đổi (trade-off / 트레이드오프)

During gap:

### Thị trường (market / 시장) thứ tự (order / 순서)

```text
Higher execution probability
Lower price certainty
```

### Limit thứ tự (order / 순서)

```text
Price protection
but may not execute
```

No thứ tự (order / 순서) kiểu (type / 타입) eliminates both price and thực thi (execution / 실행) rủi ro (risk / 위험).

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — SNB CHF Floor Removal 2015: chính sách (policy / 정책) floor, gap rủi ro (risk / 위험) và liquidity discontinuity**, **20. Thị trường (market / 시장) thứ tự (order / 순서) vs limit thứ tự (order / 순서) sự đánh đổi (trade-off / 트레이드오프)** đã nêu tiêu chí phân biệt, còn **21. Guaranteed stop is a separate sản phẩm (product / 제품) tính năng (feature / 기능)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **22. Rủi ro (risk / 위험) concentration across clients** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Guaranteed stop is a separate sản phẩm (product / 제품) tính năng (feature / 기능)

If a broker explicitly offers guaranteed-stop protection under contractual terms, economics differ.

But ordinary stop thứ tự (order / 순서) is not guaranteed stop.

Always distinguish:

```text
Stop order
Guaranteed stop product
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — SNB CHF Floor Removal 2015: chính sách (policy / 정책) floor, gap rủi ro (risk / 위험) và liquidity discontinuity**, **22. Rủi ro (risk / 위험) concentration across clients** tiếp nhận điểm tựa từ **21. Guaranteed stop is a separate sản phẩm (product / 제품) tính năng (feature / 기능)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Why backtest cannot reproduce this with ordinary candles** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Rủi ro (risk / 위험) concentration across clients

A broker may appear diversified across thousands of clients.

But if clients all use same popular chiến lược (strategy / 전략) near chính sách (policy / 정책) floor:

```text
Client count high
but factor concentration also high
```

This is same portfolio lesson at broker mức (level / 수준).

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 03 — SNB CHF Floor Removal 2015: chính sách (policy / 정책) floor, gap rủi ro (risk / 위험) và liquidity discontinuity**, **23. Why backtest cannot reproduce this with ordinary candles** tiếp nhận điểm tựa từ **22. Rủi ro (risk / 위험) concentration across clients** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Options lesson** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — SNB CHF Floor Removal 2015: chính sách (policy / 정책) floor, gap rủi ro (risk / 위험) và liquidity discontinuity**, **24. Options lesson** tiếp nhận điểm tựa từ **23. Why backtest cannot reproduce this with ordinary candles** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Central-bank balance sheet as regime variable** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — SNB CHF Floor Removal 2015: chính sách (policy / 정책) floor, gap rủi ro (risk / 위험) và liquidity discontinuity**, **25. Central-bank balance sheet as regime variable** tiếp nhận điểm tựa từ **24. Options lesson** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. What not to learn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 03 — SNB CHF Floor Removal 2015: chính sách (policy / 정책) floor, gap rủi ro (risk / 위험) và liquidity discontinuity**, **26. What not to learn** tiếp nhận điểm tựa từ **25. Central-bank balance sheet as regime variable** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. Stress-test template** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — SNB CHF Floor Removal 2015: chính sách (policy / 정책) floor, gap rủi ro (risk / 위험) và liquidity discontinuity**, **27. Stress-test template** tiếp nhận điểm tựa từ **26. What not to learn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. Cơ chế (mechanism / 메커니즘) map** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — SNB CHF Floor Removal 2015: chính sách (policy / 정책) floor, gap rủi ro (risk / 위험) và liquidity discontinuity**, **27. Stress-test template** xác định đầu vào; **28. Cơ chế (mechanism / 메커니즘) map** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **29. Practical checklist derived from the trường hợp (case / 사례)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. Cơ chế (mechanism / 메커니즘) map

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

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 03 — SNB CHF Floor Removal 2015: chính sách (policy / 정책) floor, gap rủi ro (risk / 위험) và liquidity discontinuity**, sau khi thấy quy trình trong **28. Cơ chế (mechanism / 메커니즘) map**, **29. Practical checklist derived from the trường hợp (case / 사례)** đặt nó vào một trường hợp đủ cụ thể để nhận ra điều kiện thành công và chỗ dễ sai. Từ đây, **30. Research exercise** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — SNB CHF Floor Removal 2015: chính sách (policy / 정책) floor, gap rủi ro (risk / 위험) và liquidity discontinuity**, **29. Practical checklist derived from the trường hợp (case / 사례)** cho ta quy tắc; **30. Research exercise** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Nguồn nền** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — SNB CHF Floor Removal 2015: chính sách (policy / 정책) floor, gap rủi ro (risk / 위험) và liquidity discontinuity**, **30. Research exercise** nêu điều cần giải thích; **Nguồn nền** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Nguồn nền

- Swiss National Bank, press bản phát hành (release / 릴리스), **15 January 2015 — SNB discontinues minimum exchange tỷ lệ (rate / 비율) and lowers interest tỷ lệ (rate / 비율) to -0.75%**.
- Swiss National Bank, monetary-policy chronology describing establishment and removal of the EUR/CHF minimum exchange tỷ lệ (rate / 비율).

Trường hợp (case / 사례) này tập trung vào mechanics of regime break, không dùng hindsight để khẳng định việc bỏ floor có thể được dự đoán chắc chắn.

> **Bàn giao:** Sau **Nguồn nền**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
