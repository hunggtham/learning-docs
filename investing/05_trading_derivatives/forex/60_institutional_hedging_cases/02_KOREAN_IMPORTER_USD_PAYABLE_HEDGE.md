# Trường hợp (case / 사례) 02 — Korean Importer: Hedge USD Payables và Procurement Margin

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Trường hợp (case / 사례) 02 — Korean Importer: Hedge USD Payables và Procurement Margin**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Exposure map** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Directional rủi ro (risk / 위험)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối Korean importer với USD payable hedge, để kỳ hạn thanh toán, forward và biên lợi nhuận đi cùng một kế hoạch.

Một Korean importer mua nguyên liệu/máy móc bằng USD nhưng bán sản phẩm hoặc thu doanh thu chủ yếu bằng KRW. Công ty có **economic short USD / long KRW exposure** trên khoản phải trả: nếu USD/KRW tăng, cùng một invoice USD cần nhiều KRW hơn để thanh toán.

Hedge mục tiêu (objective / 목표) là ổn định **KRW procurement chi phí (cost / 비용)**, không phải đánh cược rằng USD sẽ tăng hay giảm.

## 1. Exposure map

Giả sử:

```text
USD payable = 8,000,000 USD
Expected payment = 120 days
Functional currency = KRW
Current USD/KRW spot = 1,360
```

Unhedged KRW chi phí (cost / 비용):

```text
KRW cost = USD 8m × future USD/KRW
```

Tham chiếu (reference / 참조) at hiện tại (current / 현재) spot:

```text
8,000,000 × 1,360
= 10.88bn KRW
```

> **Nối mạch:** Trong **Trường hợp (case / 사례) 02 — Korean Importer: Hedge USD Payables và Procurement Margin**, **2. Directional rủi ro (risk / 위험)** nối từ **1. Exposure map** sang **3. Unhedged scenarios**, vì cơ chế trước tạo đầu vào cho bước sau.

## 2. Directional rủi ro (risk / 위험)

Importer bất lợi khi:

```text
USD/KRW rises
→ USD strengthens / KRW weakens
→ procurement cost in KRW rises
```

Economic exposure:

```text
Short USD
Long KRW
```

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 02 — Korean Importer: Hedge USD Payables và Procurement Margin**, **3. Unhedged scenarios** nối từ **2. Directional rủi ro (risk / 위험)** sang **4. Forward hedge**, vì cơ chế trước tạo đầu vào cho bước sau.

## 3. Unhedged scenarios

```text
USD/KRW 1,250 → 10.0bn KRW
USD/KRW 1,360 → 10.88bn KRW
USD/KRW 1,500 → 12.0bn KRW
```

Difference giữa 1,250 và 1,500 là 2.0bn KRW.

Nếu gross margin dự kiến chỉ vài tỷ KRW, currency move có thể thay đổi profitability của entire đặc tả hợp đồng (contract / 계약).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 02 — Korean Importer: Hedge USD Payables và Procurement Margin**, **4. Forward hedge** nối từ **3. Unhedged scenarios** sang **5. USD strengthens to 1,500**, vì cơ chế trước tạo đầu vào cho bước sau.

## 4. Forward hedge

Importer có thể:

```text
Buy USD forward
Sell KRW forward
```

Giả sử 4-month forward tỷ lệ (rate / 비율):

```text
USD/KRW forward = 1,370
```

Approximate locked KRW chi phí (cost / 비용):

```text
8,000,000 × 1,370
= 10.96bn KRW
```

Ignoring giao dịch (transaction / 트랜잭션)/credit details.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 02 — Korean Importer: Hedge USD Payables và Procurement Margin**, **5. USD strengthens to 1,500** nối từ **4. Forward hedge** sang **6. USD weakens to 1,250**, vì cơ chế trước tạo đầu vào cho bước sau.

## 5. USD strengthens to 1,500

Underlying payable costs:

```text
8m × 1,500 = 12.0bn KRW
```

Forward approximate gain:

```text
(1,500 - 1,370) × 8m
= +1.04bn KRW
```

Combined chi phí (cost / 비용):

```text
12.0bn - 1.04bn
≈ 10.96bn KRW
```

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 02 — Korean Importer: Hedge USD Payables và Procurement Margin**, **6. USD weakens to 1,250** nối từ **5. USD strengthens to 1,500** sang **7. Procurement pricing liên kết (connection / 연결)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 6. USD weakens to 1,250

Underlying payable costs:

```text
10.0bn KRW
```

Forward approximate mất mát (loss / 손실):

```text
(1,370 - 1,250) × 8m
= 0.96bn KRW
```

Combined:

```text
10.0bn + 0.96bn
≈ 10.96bn KRW
```

Again, derivative mất mát (loss / 손실) can indicate hedge is working.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 02 — Korean Importer: Hedge USD Payables và Procurement Margin**, sau nội dung của **6. USD weakens to 1,250**, **7. Procurement pricing liên kết (connection / 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **8. Natural hedge before derivatives** mở rộng hệ quả hoặc giới hạn liên quan.

## 7. Procurement pricing liên kết (connection / 연결)

Suppose importer signs KRW sales đặc tả hợp đồng (contract / 계약) today but USD supplier invoice is due in four months.

Without hedge:

```text
Sales price fixed in KRW
Input cost floating in USD/KRW
→ gross margin floats with FX
```

A forward can convert uncertain FX chi phí (cost / 비용) into known procurement chi phí (cost / 비용), helping price the final sản phẩm (product / 제품).

> **Nối mạch:** Trong **Trường hợp (case / 사례) 02 — Korean Importer: Hedge USD Payables và Procurement Margin**, **8. Natural hedge before derivatives** nối từ **7. Procurement pricing liên kết (connection / 연결)** sang **9. Payment certainty**, vì cơ chế trước tạo đầu vào cho bước sau.

## 8. Natural hedge before derivatives

If importer also receives USD revenue:

```text
USD payable = 8m
USD revenue = 3m
```

Net USD need is approximately:

```text
5m USD
```

Buying 8m forward ignores natural offset.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 02 — Korean Importer: Hedge USD Payables và Procurement Margin**, **9. Payment certainty** nối từ **8. Natural hedge before derivatives** sang **10. Timing rủi ro (risk / 위험) from shipment delay**, vì cơ chế trước tạo đầu vào cho bước sau.

## 9. Payment certainty

Purchase thứ tự (order / 순서) may be:

```text
firm and non-cancelable
partially cancelable
volume-dependent
subject to shipping delay
```

Hedge ratio should reflect certainty.

A 100% forward against uncertain purchase can create long USD speculation if thứ tự (order / 순서) is canceled.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 02 — Korean Importer: Hedge USD Payables và Procurement Margin**, **10. Timing rủi ro (risk / 위험) from shipment delay** nối từ **9. Payment certainty** sang **11. Early payment rủi ro (risk / 위험)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 10. Timing rủi ro (risk / 위험) from shipment delay

Expected payment day 120 may move to day 150 because shipment/customs delay.

Forward matures day 120.

Treasury may need:

```text
FX swap / forward roll
```

The hedge direction was right, but tenor mismatched actual cash luồng (flow / 흐름).

> **Nối mạch:** Trong **Trường hợp (case / 사례) 02 — Korean Importer: Hedge USD Payables và Procurement Margin**, **11. Early payment rủi ro (risk / 위험)** nối từ **10. Timing rủi ro (risk / 위험) from shipment delay** sang **12. Layered purchase hedge**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11. Early payment rủi ro (risk / 위험)

Supplier may offer discount for payment day 90 instead of 120.

Hedge maturity no longer aligns.

Closing/rolling can create mark-to-market cash flows before operating giao dịch (transaction / 트랜잭션) settles.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 02 — Korean Importer: Hedge USD Payables và Procurement Margin**, **12. Layered purchase hedge** nối từ **11. Early payment rủi ro (risk / 위험)** sang **13. Rolling hedge program**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. Layered purchase hedge

If yearly raw-material purchases are recurring:

```text
next quarter committed 90%
quarter +2 probable 60%
quarter +3 uncertain 30%
```

A layered hedge can reflect confidence by horizon.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 02 — Korean Importer: Hedge USD Payables và Procurement Margin**, **13. Rolling hedge program** nối từ **12. Layered purchase hedge** sang **14. Rolling creates đường dẫn (path / 경로) dependence**, vì cơ chế trước tạo đầu vào cho bước sau.

## 13. Rolling hedge program

For continuous imports, treasury may maintain chính sách (policy / 정책) such as:

```text
Month 1–3: 80% hedged
Month 4–6: 50%
Month 7–12: 20%
```

Each month:

```text
new forecast enters horizon
existing hedges mature
forecast updates
hedge book is rebalanced
```

This is a tiến trình (process / 프로세스), not one trade.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 02 — Korean Importer: Hedge USD Payables và Procurement Margin**, **13. Rolling hedge program** đặt đầu vào cho **14. Rolling creates đường dẫn (path / 경로) dependence**, rồi **15. Forward points affect locked chi phí (cost / 비용)** mở rộng hệ quả hoặc giới hạn liên quan.

## 14. Rolling creates đường dẫn (path / 경로) dependence

Weighted-average hedge tỷ lệ (rate / 비율) depends on when layers were added.

Two companies with same final exposure can have different hedge portfolio rates because thực thi (execution / 실행) dates differ.

Do not judge kết quả (result / 결과) from one maturity snapshot only.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 02 — Korean Importer: Hedge USD Payables và Procurement Margin**, **14. Rolling creates đường dẫn (path / 경로) dependence** đặt đầu vào cho **15. Forward points affect locked chi phí (cost / 비용)**, rồi **16. Money-market hedge intuition** mở rộng hệ quả hoặc giới hạn liên quan.

## 15. Forward points affect locked chi phí (cost / 비용)

Importer comparing spot 1,360 with forward 1,370 may say forward is “10 KRW more expensive”.

But forward points arise from relative rates/funding/basis, not merely broker markup.

Economic comparison is:

```text
Unhedged uncertain future cost
vs
known forward-locked cost
```

not `spot today vs forward` as if cash could be settled today for free.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 02 — Korean Importer: Hedge USD Payables và Procurement Margin**, **16. Money-market hedge intuition** nối từ **15. Forward points affect locked chi phí (cost / 비용)** sang **17. Option hedge**, vì cơ chế trước tạo đầu vào cho bước sau.

## 16. Money-market hedge intuition

In simplified covered-interest-parity world, importer could conceptually:

```text
borrow KRW today
buy/invest USD today
use matured USD to pay supplier
```

Forward pricing should relate to this synthetic funding đường dẫn (path / 경로).

This explains why rates enter forward tỷ lệ (rate / 비율).

> **Nối mạch:** Trong **Trường hợp (case / 사례) 02 — Korean Importer: Hedge USD Payables và Procurement Margin**, **17. Option hedge** nối từ **16. Money-market hedge intuition** sang **18. Why option can match uncertain exposure better**, vì cơ chế trước tạo đầu vào cho bước sau.

## 17. Option hedge

Importer can buy protection against USD appreciation while keeping benefit if USD falls.

Conceptually:

```text
right to buy USD at protected rate
```

This costs option premium.

Useful when amount/timing is uncertain or company values favorable FX participation.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 02 — Korean Importer: Hedge USD Payables và Procurement Margin**, **18. Why option can match uncertain exposure better** nối từ **17. Option hedge** sang **19. Premium is real ngân sách (budget / 예산) chi phí (cost / 비용)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 18. Why option can match uncertain exposure better

If purchase is canceled, a forward creates offsetting exposure that must be closed.

An option can simply expire unused, limiting downside to premium, depending on cấu trúc (structure / 구조).

Therefore optionality can have giá trị (value / 값) when underlying giao dịch (transaction / 트랜잭션) itself is uncertain.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 02 — Korean Importer: Hedge USD Payables và Procurement Margin**, **19. Premium is real ngân sách (budget / 예산) chi phí (cost / 비용)** nối từ **18. Why option can match uncertain exposure better** sang **20. Collars and structured hedges**, vì cơ chế trước tạo đầu vào cho bước sau.

## 19. Premium is real ngân sách (budget / 예산) chi phí (cost / 비용)

Option premium should be allocated into procurement economics.

Do not compare:

```text
Forward = free
Option = expensive
```

Forward has opportunity chi phí (cost / 비용)/locked payoff; option pays for asymmetry.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 02 — Korean Importer: Hedge USD Payables và Procurement Margin**, **20. Collars and structured hedges** nối từ **19. Premium is real ngân sách (budget / 예산) chi phí (cost / 비용)** sang **21. Supplier currency negotiation**, vì cơ chế trước tạo đầu vào cho bước sau.

## 20. Collars and structured hedges

A collar can finance protection by giving up benefit beyond another tỷ lệ (rate / 비율).

But structured products may add barriers/leverage/conditional notional.

Treasury must mô hình (model / 모델) full payoff, especially under large USD move.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 02 — Korean Importer: Hedge USD Payables và Procurement Margin**, **21. Supplier currency negotiation** nối từ **20. Collars and structured hedges** sang **22. Inventory holding period**, vì cơ chế trước tạo đầu vào cho bước sau.

## 21. Supplier currency negotiation

Rủi ro (risk / 위험) can be changed commercially before derivatives.

Possible đặc tả hợp đồng (contract / 계약) choices:

```text
Pay supplier in KRW
Price-adjustment clause
Split currency invoice
Shorter price validity
```

Supplier will price its own FX rủi ro (risk / 위험) into terms, so rủi ro (risk / 위험) does not disappear—it is redistributed.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 02 — Korean Importer: Hedge USD Payables và Procurement Margin**, **22. Inventory holding period** nối từ **21. Supplier currency negotiation** sang **23. Pass-through**, vì cơ chế trước tạo đầu vào cho bước sau.

## 22. Inventory holding period

Even after supplier is paid, imported inventory may be sold months later.

If final selling price can adjust with FX, economic exposure differs from a fully fixed KRW sales đặc tả hợp đồng (contract / 계약).

Treasury needs nghiệp vụ (business / 비즈니스) tiến trình (process / 프로세스) map, not invoice danh sách (list / 목록) only.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 02 — Korean Importer: Hedge USD Payables và Procurement Margin**, **23. Pass-through** nối từ **22. Inventory holding period** sang **24. Working-capital impact**, vì cơ chế trước tạo đầu vào cho bước sau.

## 23. Pass-through

If company can raise KRW selling prices after USD appreciation:

```text
FX cost shock
→ partially passed to customers
```

Then long-run economic exposure may be smaller than giao dịch (transaction / 트랜잭션) exposure suggests.

But pass-through timing and competitive các ràng buộc (constraints / 제약조건들) matter.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 02 — Korean Importer: Hedge USD Payables và Procurement Margin**, **24. Working-capital impact** nối từ **23. Pass-through** sang **25. Credit and FX tương tác (interaction / 상호작용)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 24. Working-capital impact

USD appreciation can increase KRW working-capital yêu cầu (requirement / 요구사항) before customer pricing adjusts.

Even if long-run margins recover, short-term liquidity can tighten.

Hedge can protect liquidity timing as well as accounting margin.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 02 — Korean Importer: Hedge USD Payables và Procurement Margin**, **25. Credit and FX tương tác (interaction / 상호작용)** nối từ **24. Working-capital impact** sang **26. Counterparty concentration**, vì cơ chế trước tạo đầu vào cho bước sau.

## 25. Credit and FX tương tác (interaction / 상호작용)

If supplier requires margin/prepayment when thị trường (market / 시장) stress rises:

```text
USD strengthens
+ payment terms tighten
→ KRW liquidity need rises twice
```

FX hedge alone may not cover supplier-credit shock.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 02 — Korean Importer: Hedge USD Payables và Procurement Margin**, **26. Counterparty concentration** nối từ **25. Credit and FX tương tác (interaction / 상호작용)** sang **27. Settlement rủi ro (risk / 위험)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 26. Counterparty concentration

If all forwards are with one bank:

```text
credit line / operational outage
```

can impair hedge program.

Large corporate treasury often tracks counterparty limits.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 02 — Korean Importer: Hedge USD Payables và Procurement Margin**, **27. Settlement rủi ro (risk / 위험)** nối từ **26. Counterparty concentration** sang **28. Cash-flow-at-risk view**, vì cơ chế trước tạo đầu vào cho bước sau.

## 27. Settlement rủi ro (risk / 위험)

Deliverable forward requires actual currency settlement.

Treasury must coordinate:

```text
bank account
value date
cutoff time
payment instruction
supplier settlement
```

A correctly priced hedge can thất bại (fail / 실패) operationally if payment tiến trình (process / 프로세스) fails.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 02 — Korean Importer: Hedge USD Payables và Procurement Margin**, **27. Settlement rủi ro (risk / 위험)** đặt đầu vào cho **28. Cash-flow-at-risk view**, rồi **29. Ngân sách (budget / 예산) tỷ lệ (rate / 비율) vs thị trường (market / 시장) tỷ lệ (rate / 비율)** mở rộng hệ quả hoặc giới hạn liên quan.

## 28. Cash-flow-at-risk view

Instead of focusing only on P/L, measure:

```text
KRW cash needed at payment date
```

under scenarios.

Hedge chính sách (policy / 정책) can mục tiêu (target / 대상) maximum acceptable cash-flow-at-risk.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 02 — Korean Importer: Hedge USD Payables và Procurement Margin**, **28. Cash-flow-at-risk view** đặt đầu vào cho **29. Ngân sách (budget / 예산) tỷ lệ (rate / 비율) vs thị trường (market / 시장) tỷ lệ (rate / 비율)**, rồi **30. Over-hedge example** mở rộng hệ quả hoặc giới hạn liên quan.

## 29. Ngân sách (budget / 예산) tỷ lệ (rate / 비율) vs thị trường (market / 시장) tỷ lệ (rate / 비율)

Nghiệp vụ (business / 비즈니스) plan may assume:

```text
USD/KRW budget = 1,400
```

Treasury hedges at weighted 1,370.

This may create procurement margin buffer relative to ngân sách (budget / 예산), but it is not trading alpha.

Ngân sách (budget / 예산) tỷ lệ (rate / 비율) is nội bộ (internal / 내부) quyết định (decision / 결정) benchmark.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 02 — Korean Importer: Hedge USD Payables và Procurement Margin**, **29. Ngân sách (budget / 예산) tỷ lệ (rate / 비율) vs thị trường (market / 시장) tỷ lệ (rate / 비율)** nêu quy tắc; **30. Over-hedge example** thử quy tắc trong tình huống, rồi **31. Under-hedge example** mở rộng hệ quả.

## 30. Over-hedge example

Forecast import USD 8m.

Actual purchase only USD 5m.

Forward buy USD 8m remains.

Net after paying supplier:

```text
+3m USD excess
```

Treasury must sell excess USD, exposing company to closeout P/L.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 02 — Korean Importer: Hedge USD Payables và Procurement Margin**, **30. Over-hedge example** nêu quy tắc; **31. Under-hedge example** thử quy tắc trong tình huống, rồi **32. Forecast-quality vòng phản hồi (feedback loop / 피드백 루프)** mở rộng hệ quả.

## 31. Under-hedge example

Actual purchase becomes USD 10m while forward covers USD 8m.

Remaining:

```text
2m USD unhedged
```

If USD spikes, residual chi phí (cost / 비용) can still be material.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 02 — Korean Importer: Hedge USD Payables và Procurement Margin**, **31. Under-hedge example** nêu quy tắc; **32. Forecast-quality vòng phản hồi (feedback loop / 피드백 루프)** thử quy tắc trong tình huống, rồi **33. Scenario ma trận (matrix / 행렬)** mở rộng hệ quả.

## 32. Forecast-quality vòng phản hồi (feedback loop / 피드백 루프)

Hedge effectiveness depends on procurement forecast chất lượng (quality / 품질).

Nhánh học (track / 트랙):

```text
forecast vs actual amount
forecast vs actual payment date
```

Improving supply-chain forecast can reduce FX rủi ro (risk / 위험) as much as changing derivative instrument.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 02 — Korean Importer: Hedge USD Payables và Procurement Margin**, **33. Scenario ma trận (matrix / 행렬)** nối từ **32. Forecast-quality vòng phản hồi (feedback loop / 피드백 루프)** sang **34. Stress — USD spike + purchase increase**, vì cơ chế trước tạo đầu vào cho bước sau.

## 33. Scenario ma trận (matrix / 행렬)

Kiểm thử (test / 테스트):

```text
USD/KRW = 1,200 / 1,350 / 1,500 / 1,650
Purchase amount = 60% / 100% / 130% forecast
Payment delay = -30 / 0 / +30 days
```

Compute:

```text
Underlying KRW cost
Hedge P/L
Option premium if applicable
Roll cost
Over/under hedge
Total procurement cash cost
```

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 02 — Korean Importer: Hedge USD Payables và Procurement Margin**, **34. Stress — USD spike + purchase increase** nối từ **33. Scenario ma trận (matrix / 행렬)** sang **35. Stress — thứ tự (order / 순서) cancellation + USD spike**, vì cơ chế trước tạo đầu vào cho bước sau.

## 34. Stress — USD spike + purchase increase

This is worst combination:

```text
USD/KRW rises
and
actual import amount exceeds forecast
```

Residual unhedged amount faces high spot tỷ lệ (rate / 비율).

Rủi ro (risk / 위험) management must stress volume and tỷ lệ (rate / 비율) jointly.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 02 — Korean Importer: Hedge USD Payables và Procurement Margin**, **35. Stress — thứ tự (order / 순서) cancellation + USD spike** nối từ **34. Stress — USD spike + purchase increase** sang **36. Hedge attribution**, vì cơ chế trước tạo đầu vào cho bước sau.

## 35. Stress — thứ tự (order / 순서) cancellation + USD spike

If purchase canceled but forward remains, company long USD via hedge.

USD spike may create gain, but that is accidental speculation after nghiệp vụ (business / 비즈니스) exposure disappeared.

Chính sách (policy / 정책) should require prompt exposure/hedge reconciliation.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 02 — Korean Importer: Hedge USD Payables và Procurement Margin**, **36. Hedge attribution** nối từ **35. Stress — thứ tự (order / 순서) cancellation + USD spike** sang **37. Procurement hedge dashboard**, vì cơ chế trước tạo đầu vào cho bước sau.

## 36. Hedge attribution

Rà soát (review / 검토):

```text
Unhedged procurement FX effect
+ Forward/option P/L
+ Premium
+ Roll cost
+ Spread/fees
+ Forecast mismatch
= Hedged procurement result
```

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 02 — Korean Importer: Hedge USD Payables và Procurement Margin**, **37. Procurement hedge dashboard** nối từ **36. Hedge attribution** sang **38. What not to learn**, vì cơ chế trước tạo đầu vào cho bước sau.

## 37. Procurement hedge dashboard

```text
Supplier
Currency
Committed payable
Forecast payable
Natural offsets
Hedge notional
Hedge ratio
Maturity
Weighted hedge rate
Payment-date mismatch
Counterparty
Residual stress cost
```

> **Nối mạch:** Trong **Trường hợp (case / 사례) 02 — Korean Importer: Hedge USD Payables và Procurement Margin**, **38. What not to learn** nối từ **37. Procurement hedge dashboard** sang **39. Trường hợp (case / 사례) outputs**, vì cơ chế trước tạo đầu vào cho bước sau.

## 38. What not to learn

Wrong:

```text
Importer should always buy USD early when USD looks cheap.
```

That is a thị trường (market / 시장) view, not hedge chính sách (policy / 정책).

Wrong:

```text
Option is always safer than forward.
```

Options have premium, liquidity, valuation and cấu trúc (structure / 구조) rủi ro (risk / 위험).

Better:

```text
Instrument and hedge ratio must fit certainty, horizon,
cash-flow objective and residual-risk tolerance.
```

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 02 — Korean Importer: Hedge USD Payables và Procurement Margin**, **38. What not to learn** nêu quy tắc; **39. Trường hợp (case / 사례) outputs** thử quy tắc trong tình huống, rồi **40. Rà soát (review / 검토) questions** mở rộng hệ quả.

## 39. Trường hợp (case / 사례) outputs

Create:

```text
importer_exposure_map.md
payment_timeline.md
layered_import_hedge_policy.md
procurement_scenario_matrix.md
cash_flow_at_risk_report.md
hedge_effectiveness_report.md
```

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 02 — Korean Importer: Hedge USD Payables và Procurement Margin**, **39. Trường hợp (case / 사례) outputs** nêu quy tắc; **40. Rà soát (review / 검토) questions** thử quy tắc trong tình huống, rồi **Nội bộ (internal / 내부) links** mở rộng hệ quả.

## 40. Rà soát (review / 검토) questions

You should explain:

1. Why importer is short USD economically.
2. Why natural USD revenue reduces derivative need.
3. Why delayed shipment creates roll rủi ro (risk / 위험).
4. Why option can be useful when purchase amount is uncertain.
5. Why forward points belong to funding economics.
6. Why procurement forecast accuracy is part of FX rủi ro (risk / 위험) management.
7. Why combined underlying + hedge kết quả (result / 결과) matters more than derivative P/L.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 02 — Korean Importer: Hedge USD Payables và Procurement Margin**, **Nội bộ (internal / 내부) links** nối từ **40. Rà soát (review / 검토) questions** sang  Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Nội bộ (internal / 내부) links

- [Funding, NDF, basis and forward curve](../90_connections/00_FX_FUNDING_NDF_BASIS_AND_FORWARD_CURVE.md)
- [Portfolio FX risk](../11_PORTFOLIO_FX_RISK_CORRELATION_AND_FACTOR_EXPOSURE.md)
- [FX options and hedging](../14_FX_OPTIONS_VOLATILITY_AND_HEDGING.md)

> **Bàn giao:** Sau **Nội bộ (internal / 내부) links**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
