# Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Nghiệp vụ (business / 비즈니스) bài toán (problem / 문제)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Direct USD borrowing** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối cross-currency funding với debt hedge, để khớp dòng tiền, basis và kỳ hạn thay vì chỉ khóa một tỷ giá danh nghĩa.

Một company hoặc financial institution có thể huy động vốn ở currency A nhưng thực sự cần economic funding ở currency B. Khi đó FX derivatives không chỉ hedge price rủi ro (risk / 위험); chúng **biến đổi currency của liabilities và funding cash flows**.

Mô hình tư duy (mental model / 사고 모델):

```text
Debt raised in Currency A
+ FX / Cross-Currency Hedge
→ Synthetic Funding in Currency B
```

Điểm quan trọng là so **all-in synthetic funding chi phí (cost / 비용)** với direct funding, đồng thời tính collateral, rollover, basis, counterparty và liquidity rủi ro (risk / 위험).

## 1. Nghiệp vụ (business / 비즈니스) bài toán (problem / 문제)

Giả sử Korean company cần equivalent:

```text
USD 100m funding
for 3 years
```

Nhưng company có thể phát hành KRW bonds với investor demand tốt hơn.

Two alternatives:

```text
A. Borrow USD directly
B. Borrow KRW, then swap KRW funding into USD
```

Choice không nên dựa chỉ vào headline coupon.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **2. Direct USD borrowing** nối từ **1. Nghiệp vụ (business / 비즈니스) bài toán (problem / 문제)** sang **3. KRW borrowing tuyến (route / 경로)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 2. Direct USD borrowing

Suppose:

```text
USD debt principal = 100m
USD interest = SOFR + credit spread
```

Company has direct USD liability.

If nghiệp vụ (business / 비즈니스) cash flows are in USD, this may naturally match funding need.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **3. KRW borrowing tuyến (route / 경로)** nối từ **2. Direct USD borrowing** sang **4. Cross-currency swap concept**, vì cơ chế trước tạo đầu vào cho bước sau.

## 3. KRW borrowing tuyến (route / 경로)

Company issues KRW debt:

```text
KRW principal equivalent to USD 100m
KRW coupon/floating cost
```

But dự án (project / 프로젝트) needs USD cash.

At inception, company can swap KRW into USD.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **4. Cross-currency swap concept** nối từ **3. KRW borrowing tuyến (route / 경로)** sang **5. Why not just spot-convert KRW into USD?**, vì cơ chế trước tạo đầu vào cho bước sau.

## 4. Cross-currency swap concept

A cross-currency swap may exchange:

```text
Principal at start
Periodic interest cash flows
Principal back at maturity
```

in two currencies.

Simplified:

```text
Company pays USD leg
Company receives KRW leg
```

so KRW debt dịch vụ (service / 서비스) is economically offset while company bears synthetic USD funding.

Chính xác (exact / 정확한) convention depends on đặc tả hợp đồng (contract / 계약).

> **Nối mạch:** Trong **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **5. Why not just spot-convert KRW into USD?** nối từ **4. Cross-currency swap concept** sang **6. Synthetic funding chi phí (cost / 비용)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 5. Why not just spot-convert KRW into USD?

If company sells KRW for USD at inception but keeps unhedged KRW debt:

```text
Assets/use of funds = USD
Liability = KRW
```

Future principal repayment creates FX mismatch.

Cross-currency hedge transforms future cash flows too.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **6. Synthetic funding chi phí (cost / 비용)** nối từ **5. Why not just spot-convert KRW into USD?** sang **7. Covered interest parity intuition**, vì cơ chế trước tạo đầu vào cho bước sau.

## 6. Synthetic funding chi phí (cost / 비용)

All-in synthetic USD funding roughly reflects:

```text
KRW borrowing cost
+ cross-currency swap/basis economics
+ transaction/credit/collateral cost
```

Not simply KRW coupon translated at spot.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **7. Covered interest parity intuition** nối từ **6. Synthetic funding chi phí (cost / 비용)** sang **8. Cross-currency basis**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7. Covered interest parity intuition

In frictionless world, FX forward/swaps align currency funding returns.

If synthetic USD were persistently much cheaper than direct USD with no các ràng buộc (constraints / 제약조건들):

```text
arbitrage demand should compress gap
```

Real markets have balance-sheet, collateral, regulatory and credit frictions.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **8. Cross-currency basis** nối từ **7. Covered interest parity intuition** sang **9. Funding currency vs reporting currency**, vì cơ chế trước tạo đầu vào cho bước sau.

## 8. Cross-currency basis

Basis represents deviation/adjustment needed beyond simple interest differential in swap pricing.

It can reflect:

```text
relative demand for currency funding
dealer balance-sheet cost
collateral terms
credit/regulatory constraints
market segmentation
```

Basis is economics, not automatically arbitrage profit.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **9. Funding currency vs reporting currency** nối từ **8. Cross-currency basis** sang **10. Natural hedge through revenue**, vì cơ chế trước tạo đầu vào cho bước sau.

## 9. Funding currency vs reporting currency

Company may report in KRW but dự án (project / 프로젝트) cash luồng (flow / 흐름) in USD.

Best liability currency depends on economic matching, not reporting currency alone.

Questions:

```text
Where does revenue arrive?
Where are costs paid?
What currency services debt?
What happens under stress?
```

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **10. Natural hedge through revenue** nối từ **9. Funding currency vs reporting currency** sang **11. Example capital cấu trúc (structure / 구조)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 10. Natural hedge through revenue

If dự án (project / 프로젝트) generates stable USD revenue:

```text
USD debt
→ paid from USD revenue
```

can reduce giao dịch (transaction / 트랜잭션) FX rủi ro (risk / 위험).

But if revenue is only partially USD or cyclical, mismatch remains.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **10. Natural hedge through revenue** nêu quy tắc; **11. Example capital cấu trúc (structure / 구조)** thử quy tắc trong tình huống, rồi **12. Do not use spot movement to judge swap alone** mở rộng hệ quả.

## 11. Example capital cấu trúc (structure / 구조)

Suppose:

```text
KRW bond proceeds = 136bn KRW
Spot USD/KRW = 1,360
USD received through swap ≈ 100m USD
Tenor = 3 years
```

Cross-currency swap maps KRW debt cash flows into agreed USD cash flows.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **11. Example capital cấu trúc (structure / 구조)** nêu quy tắc; **12. Do not use spot movement to judge swap alone** thử quy tắc trong tình huống, rồi **13. Mark-to-market vs cash-flow mục tiêu (objective / 목표)** mở rộng hệ quả.

## 12. Do not use spot movement to judge swap alone

If USD/KRW rises sharply, mark-to-market of swap can move significantly.

But company also has debt/assets whose economic values move.

Evaluate combined funding gói (package / 패키지).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **12. Do not use spot movement to judge swap alone** đặt đầu vào cho **13. Mark-to-market vs cash-flow mục tiêu (objective / 목표)**, rồi **14. Collateral mechanics** mở rộng hệ quả hoặc giới hạn liên quan.

## 13. Mark-to-market vs cash-flow mục tiêu (objective / 목표)

Treasury may intend to hold swap to maturity.

Still, mark-to-market matters for:

```text
collateral
credit limits
accounting/reporting
termination cost
```

Economic cash-flow hedge can create interim liquidity needs.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **13. Mark-to-market vs cash-flow mục tiêu (objective / 목표)** đặt đầu vào cho **14. Collateral mechanics**, rồi **15. Wrong-way liquidity rủi ro (risk / 위험)** mở rộng hệ quả hoặc giới hạn liên quan.

## 14. Collateral mechanics

Under collateral agreement, adverse swap MTM can require cash/securities.

This creates:

```text
market move
→ collateral call
→ liquidity need
```

Even if final maturity cash flows remain economically matched.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **15. Wrong-way liquidity rủi ro (risk / 위험)** nối từ **14. Collateral mechanics** sang **16. Counterparty credit rủi ro (risk / 위험)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 15. Wrong-way liquidity rủi ro (risk / 위험)

Stress can produce:

```text
business cash flow weakens
+ swap collateral call increases
+ funding markets tighten
```

Treasury must stress combined liquidity, not each item separately.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **16. Counterparty credit rủi ro (risk / 위험)** nối từ **15. Wrong-way liquidity rủi ro (risk / 위험)** sang **17. Replacement rủi ro (risk / 위험)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 16. Counterparty credit rủi ro (risk / 위험)

OTC cross-currency swap exposes company to bank/dealer counterparty.

Rủi ro (risk / 위험) management includes:

```text
legal agreement
netting
collateral
counterparty limits
replacement cost
```

A 3-year hedge has longer counterparty horizon than 1-month forward.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **17. Replacement rủi ro (risk / 위험)** nối từ **16. Counterparty credit rủi ro (risk / 위험)** sang **18. Maturity mismatch**, vì cơ chế trước tạo đầu vào cho bước sau.

## 17. Replacement rủi ro (risk / 위험)

If counterparty defaults when swap is valuable to company:

```text
company must replace hedge at current market rate
```

Replacement chi phí (cost / 비용) can be material.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **18. Maturity mismatch** nối từ **17. Replacement rủi ro (risk / 위험)** sang **19. Rollover basis rủi ro (risk / 위험)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 18. Maturity mismatch

Suppose debt is 5 years but hedge is 3 years.

At year 3:

```text
hedge expires
2 years debt remain
```

Company faces roll/refinancing rủi ro (risk / 위험) for hedge.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **19. Rollover basis rủi ro (risk / 위험)** nối từ **18. Maturity mismatch** sang **20. Debt refinancing rủi ro (risk / 위험)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 19. Rollover basis rủi ro (risk / 위험)

Future swap basis may be very different.

A chiến lược (strategy / 전략) that looks cheap today because 3-year basis is favorable may become expensive when rolled.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **20. Debt refinancing rủi ro (risk / 위험)** nối từ **19. Rollover basis rủi ro (risk / 위험)** sang **21. Lời gọi (call / 호출)/put features in debt**, vì cơ chế trước tạo đầu vào cho bước sau.

## 20. Debt refinancing rủi ro (risk / 위험)

Even with 5-year hedge matching 5-year debt, company may refinance debt early or repay early.

If hedge remains:

```text
orphan derivative exposure
```

must be closed/restructured.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **21. Lời gọi (call / 호출)/put features in debt** nối từ **20. Debt refinancing rủi ro (risk / 위험)** sang **22. Floating vs fixed legs**, vì cơ chế trước tạo đầu vào cho bước sau.

## 21. Lời gọi (call / 호출)/put features in debt

Callable debt or prepayment optionality creates uncertain liability horizon.

Fixed hedge maturity can become mismatched.

Instrument optionality and hedge optionality should be considered together.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **22. Floating vs fixed legs** nối từ **21. Lời gọi (call / 호출)/put features in debt** sang **23. Interest-rate swap combination**, vì cơ chế trước tạo đầu vào cho bước sau.

## 22. Floating vs fixed legs

Cross-currency swap can exchange:

```text
fixed vs fixed
fixed vs floating
floating vs floating
```

Funding transformation includes both:

```text
currency risk
and
interest-rate risk
```

Do not discuss currency leg while ignoring tỷ lệ (rate / 비율) reset cấu trúc (structure / 구조).

> **Nối mạch:** Trong **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **23. Interest-rate swap combination** nối từ **22. Floating vs fixed legs** sang **24. DV01 and FX delta**, vì cơ chế trước tạo đầu vào cho bước sau.

## 23. Interest-rate swap combination

Treasury may use multiple derivatives:

```text
Cross-currency swap
+ interest-rate swap
```

or one cấu trúc (structure / 구조) that transforms both currency and tỷ lệ (rate / 비율) basis.

Rủi ro (risk / 위험) hệ thống (system / 시스템) should consolidate sensitivities.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **24. DV01 and FX delta** nối từ **23. Interest-rate swap combination** sang **25. Basis sensitivity**, vì cơ chế trước tạo đầu vào cho bước sau.

## 24. DV01 and FX delta

Funding hedge can carry:

```text
FX delta
interest-rate DV01 by currency
basis sensitivity
```

A “currency hedge” can still have substantial rates/basis rủi ro (risk / 위험).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **25. Basis sensitivity** nối từ **24. DV01 and FX delta** sang **26. NDF/funding limitation**, vì cơ chế trước tạo đầu vào cho bước sau.

## 25. Basis sensitivity

If cross-currency basis widens, swap MTM changes even if spot FX stays unchanged.

This is why funding hedge cannot be monitored by spot chart alone.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **25. Basis sensitivity** đặt tiêu chí; **26. NDF/funding limitation** dùng tiêu chí đó để kiểm tra ranh giới, rồi **27. FX swap for short-term funding** mở rộng hệ quả.

## 26. NDF/funding limitation

NDF hedges exchange-rate settlement but does not necessarily provide vật lý (physical / 물리적) currency funding.

If company needs actual USD cash:

```text
NDF P/L
≠ USD funding itself
```

This distinction is trọng yếu (critical / 중요) in restricted/onshore-offshore markets.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **26. NDF/funding limitation** đặt tiêu chí; **27. FX swap for short-term funding** dùng tiêu chí đó để kiểm tra ranh giới, rồi **28. FX swap rollover** mở rộng hệ quả.

## 27. FX swap for short-term funding

For shorter horizon, institution can use FX swap:

```text
Near leg: obtain USD now
Far leg: return USD / receive KRW later
```

This transforms temporary liquidity.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **28. FX swap rollover** nối từ **27. FX swap for short-term funding** sang **29. 2020 lesson**, vì cơ chế trước tạo đầu vào cho bước sau.

## 28. FX swap rollover

Rolling overnight/1m/3m funding creates maturity mismatch if underlying asset is long-term.

```text
long asset
funded by short FX swaps
```

can be vulnerable to rollover freeze.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **29. 2020 lesson** nối từ **28. FX swap rollover** sang **30. Reserve/corporate distinction**, vì cơ chế trước tạo đầu vào cho bước sau.

## 29. 2020 lesson

Toàn cục (global / 전역) USD funding stress showed that:

```text
USD availability
and
cross-currency funding cost
```

can thay đổi (change / 변경) rapidly under hệ thống (system / 시스템) stress.

A normal-times synthetic funding advantage may disappear when needed most.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **30. Reserve/corporate distinction** nối từ **29. 2020 lesson** sang **31. All-in funding comparison**, vì cơ chế trước tạo đầu vào cho bước sau.

## 30. Reserve/corporate distinction

Central-bank swap lines can improve hệ thống (system / 시스템) USD liquidity, but private company truy cập (access / 접근) is indirect through domestic financial hệ thống (system / 시스템) and program rules.

Do not assume central-bank facility guarantees company funding.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **31. All-in funding comparison** nối từ **30. Reserve/corporate distinction** sang **32. Cheap funding can be compensation for hidden rủi ro (risk / 위험)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 31. All-in funding comparison

Create ma trận (matrix / 행렬):

```text
Direct USD debt
KRW debt + CCS
KRW debt + rolling FX swaps
Other market route
```

Compare:

```text
coupon/reference rate
credit spread
basis
transaction cost
collateral liquidity
roll risk
counterparty risk
market-access risk
```

> **Nối mạch:** Trong **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **32. Cheap funding can be compensation for hidden rủi ro (risk / 위험)** nối từ **31. All-in funding comparison** sang **33. Term funding premium**, vì cơ chế trước tạo đầu vào cho bước sau.

## 32. Cheap funding can be compensation for hidden rủi ro (risk / 위험)

If rolling short-dated swaps looks cheaper than 5-year fixed CCS:

```text
lower current cost
may reflect taking future rollover/basis risk
```

Do not compare expected chi phí (cost / 비용) without rủi ro (risk / 위험) horizon.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **33. Term funding premium** nối từ **32. Cheap funding can be compensation for hidden rủi ro (risk / 위험)** sang **34. Liquidity stress scenario**, vì cơ chế trước tạo đầu vào cho bước sau.

## 33. Term funding premium

Longer hedge tenor often embeds liquidity/credit/basis conditions for longer horizon.

Paying more can buy certainty.

Treasury choice is rủi ro (risk / 위험) allocation, not only price tối ưu hóa (optimization / 최적화).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **34. Liquidity stress scenario** nối từ **33. Term funding premium** sang **35. Revenue shock scenario**, vì cơ chế trước tạo đầu vào cho bước sau.

## 34. Liquidity stress scenario

Assume:

```text
USD/KRW +15%
Cross-currency basis moves adversely
USD funding spread +200 bp
Collateral call = 10m USD
New FX-swap tenor available only 1 month
```

Calculate whether company can meet:

```text
collateral
interest
principal/roll needs
```

> **Nối mạch:** Trong **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **35. Revenue shock scenario** nối từ **34. Liquidity stress scenario** sang **36. Early termination scenario**, vì cơ chế trước tạo đầu vào cho bước sau.

## 35. Revenue shock scenario

USD dự án (project / 프로젝트) revenue falls 40% while USD debt dịch vụ (service / 서비스) unchanged.

Natural hedge deteriorates.

Currency-matched debt does not remove business-volume rủi ro (risk / 위험).

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **36. Early termination scenario** nối từ **35. Revenue shock scenario** sang **37. Counterparty thất bại (failure / 실패) scenario**, vì cơ chế trước tạo đầu vào cho bước sau.

## 36. Early termination scenario

Dự án (project / 프로젝트) is sold after 18 months.

Debt prepaid, but 3-year cross-currency swap remains.

Need compute termination giá trị (value / 값) and liquidity impact.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **37. Counterparty thất bại (failure / 실패) scenario** nối từ **36. Early termination scenario** sang **38. Multi-counterparty chiến lược (strategy / 전략)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 37. Counterparty thất bại (failure / 실패) scenario

Bank counterparty defaults when hedge is positive MTM to company.

Company must replace at stressed thị trường (market / 시장) terms.

Stress:

```text
replacement spread
basis
legal closeout delay
```

> **Nối mạch:** Trong **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **38. Multi-counterparty chiến lược (strategy / 전략)** nối từ **37. Counterparty thất bại (failure / 실패) scenario** sang **39. Collateral currency**, vì cơ chế trước tạo đầu vào cho bước sau.

## 38. Multi-counterparty chiến lược (strategy / 전략)

Splitting hedge among banks can reduce concentration but increases:

```text
legal documentation
operational complexity
netting fragmentation
```

Diversification has chi phí (cost / 비용).

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **39. Collateral currency** nối từ **38. Multi-counterparty chiến lược (strategy / 전략)** sang **40. Hedge accounting ranh giới (boundary / 경계)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 39. Collateral currency

Collateral posted in different currency can itself create FX/funding need.

CSA terms are part of economics.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **39. Collateral currency** đặt tiêu chí; **40. Hedge accounting ranh giới (boundary / 경계)** dùng tiêu chí đó để kiểm tra ranh giới, rồi **41. Regulatory/truy cập (access / 접근) ranh giới (boundary / 경계)** mở rộng hệ quả.

## 40. Hedge accounting ranh giới (boundary / 경계)

Accounting designation can affect P&L presentation, but economic hedge should first be understood as cash-flow/balance-sheet transformation.

Professional hiện thực (implementation / 구현) requires hiện tại (current / 현재) accounting and legal rà soát (review / 검토) separately.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **40. Hedge accounting ranh giới (boundary / 경계)** đặt tiêu chí; **41. Regulatory/truy cập (access / 접근) ranh giới (boundary / 경계)** dùng tiêu chí đó để kiểm tra ranh giới, rồi **42. Funding attribution** mở rộng hệ quả.

## 41. Regulatory/truy cập (access / 접근) ranh giới (boundary / 경계)

Cross-border derivatives truy cập (access / 접근) depends on:

```text
entity type
jurisdiction
product
reporting
collateral/legal framework
```

Korea/Vietnam-specific rules should be verified from hiện tại (current / 현재) official sources before real use.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **41. Regulatory/truy cập (access / 접근) ranh giới (boundary / 경계)** đặt tiêu chí; **42. Funding attribution** dùng tiêu chí đó để kiểm tra ranh giới, rồi **43. Hiệu năng (performance / 성능) vs rủi ro (risk / 위험) mục tiêu (objective / 목표)** mở rộng hệ quả.

## 42. Funding attribution

Treasury should decompose:

```text
Base borrowing cost
Credit spread
Cross-currency basis
Hedge execution cost
Collateral funding cost
Roll cost
Early termination cost
```

Without decomposition, “synthetic USD chi phí (cost / 비용)” is opaque.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **43. Hiệu năng (performance / 성능) vs rủi ro (risk / 위험) mục tiêu (objective / 목표)** nối từ **42. Funding attribution** sang **44. Balance-sheet exposure map**, vì cơ chế trước tạo đầu vào cho bước sau.

## 43. Hiệu năng (performance / 성능) vs rủi ro (risk / 위험) mục tiêu (objective / 목표)

A funding hedge can look expensive ex post if currency moved favorably.

But mục tiêu (objective / 목표) may be:

```text
ensure debt-service capacity
and remove FX mismatch
```

Evaluate against rủi ro (risk / 위험) mục tiêu (objective / 목표), not hindsight spot tỷ lệ (rate / 비율).

> **Nối mạch:** Trong **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **44. Balance-sheet exposure map** nối từ **43. Hiệu năng (performance / 성능) vs rủi ro (risk / 위험) mục tiêu (objective / 목표)** sang **45. Maturity ladder**, vì cơ chế trước tạo đầu vào cho bước sau.

## 44. Balance-sheet exposure map

Create:

```text
Assets by currency
Revenue by currency
Operating costs by currency
Debt by currency
Derivative legs
Collateral currency
Liquidity reserves
Maturity buckets
```

This map should precede derivative choice.

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **45. Maturity ladder** nối từ **44. Balance-sheet exposure map** sang **46. Sensitivity dashboard**, vì cơ chế trước tạo đầu vào cho bước sau.

## 45. Maturity ladder

Bucket:

```text
0–1m
1–3m
3–12m
1–3y
3y+
```

for debt, derivatives and expected cash flows.

Funding rủi ro (risk / 위험) often hides in maturity mismatch rather than net currency exposure.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **46. Sensitivity dashboard** nối từ **45. Maturity ladder** sang **47. What not to learn**, vì cơ chế trước tạo đầu vào cho bước sau.

## 46. Sensitivity dashboard

Monitor:

```text
FX delta by currency
Rate DV01 by currency
Cross-currency basis sensitivity
Collateral requirement
Counterparty exposure
Refinancing amount by horizon
```

> **Nối mạch:** Trong **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **47. What not to learn** nối từ **46. Sensitivity dashboard** sang **48. Trường hợp (case / 사례) outputs**, vì cơ chế trước tạo đầu vào cho bước sau.

## 47. What not to learn

Wrong:

```text
Borrow wherever coupon is lowest.
```

Wrong:

```text
Cross-currency swap eliminates funding risk.
```

Wrong:

```text
NDF is equivalent to physical USD funding.
```

Better:

```text
Compare all-in synthetic funding cost together with
basis, collateral, rollover, counterparty and maturity risk.
```

> **Nối mạch:** Ở chặng này của **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **47. What not to learn** nêu quy tắc; **48. Trường hợp (case / 사례) outputs** thử quy tắc trong tình huống, rồi **49. Rà soát (review / 검토) questions** mở rộng hệ quả.

## 48. Trường hợp (case / 사례) outputs

Create:

```text
funding_currency_map.md
asset_liability_maturity_ladder.md
direct_vs_synthetic_funding_matrix.md
cross_currency_swap_cashflow_map.md
basis_collateral_stress_test.md
counterparty_limit_report.md
funding_cost_attribution.md
```

> **Nối mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **48. Trường hợp (case / 사례) outputs** nêu quy tắc; **49. Rà soát (review / 검토) questions** thử quy tắc trong tình huống, rồi **Nội bộ (internal / 내부) links** mở rộng hệ quả.

## 49. Rà soát (review / 검토) questions

Explain:

1. Why debt currency should be compared with cash-flow currency.
2. Why spot conversion alone does not hedge future liability cash flows.
3. Why cross-currency basis enters synthetic funding chi phí (cost / 비용).
4. Why economically hedged swap can still create collateral liquidity stress.
5. Why short FX-swap funding against long assets creates rollover rủi ro (risk / 위험).
6. Why NDF hedge is not vật lý (physical / 물리적) funding.
7. Why all-in funding chi phí (cost / 비용) must include hidden rủi ro (risk / 위험), not coupon only.

> **Nối mạch:** Trong **Trường hợp (case / 사례) 04 — Cross-Currency Funding: Debt, FX Swap và Basis Rủi ro (risk / 위험)**, **Nội bộ (internal / 내부) links** nối từ **49. Rà soát (review / 검토) questions** sang  Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Nội bộ (internal / 내부) links

- [Funding, NDF, basis and forward curve](../90_connections/00_FX_FUNDING_NDF_BASIS_AND_FORWARD_CURVE.md)
- [2020 global USD funding stress](../80_case_studies/04_GLOBAL_USD_FUNDING_STRESS_2020.md)
- [Portfolio FX risk](../11_PORTFOLIO_FX_RISK_CORRELATION_AND_FACTOR_EXPOSURE.md)

> **Bàn giao:** Sau **Nội bộ (internal / 내부) links**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
