# Case 05 — Thu nhập tăng và muốn mua xe: tránh biến lifestyle upgrade thành fixed-cost trap

## Bối cảnh

Thu nhập take-home của một người tăng từ 3.8 triệu lên 5.0 triệu KRW/tháng. Sau vài tháng, người này muốn đổi từ public transport sang một chiếc xe mới và thấy monthly payment “chỉ” khoảng 700 nghìn KRW.

Case này không hỏi chiếc xe nào tốt. Câu hỏi là: **income tăng 1.2 triệu KRW/tháng có thật sự tạo đủ capacity cho toàn bộ cost structure của car ownership hay chỉ đủ cho loan payment hiển thị?**

## 1. Monthly payment không phải total cost

Một chiếc xe tạo nhiều cash outflow:

```text
loan / lease payment
insurance
fuel / charging
parking
maintenance
tires / consumables
registration / taxes / inspection depending on jurisdiction
repairs
depreciation
opportunity cost of down payment
```

Nếu chỉ nhìn 700k payment, household đang đánh giá financing product chứ chưa đánh giá car ownership.

## 2. Xây total-cost-of-ownership budget

Ví dụ minh họa:

```text
Loan payment       0.70m
Insurance          0.15m
Fuel               0.18m
Parking            0.12m
Maintenance reserve 0.10m
-------------------------
Cash cost          1.25m/month
```

Thu nhập tăng 1.2m nhưng car cash cost ước tính 1.25m. Như vậy toàn bộ salary increase bị hấp thụ, thậm chí household margin nhỏ hơn trước.

Chưa tính depreciation.

## 3. Depreciation là economic cost dù không có monthly bill

Giả sử xe mua 35m KRW và sau vài năm market value giảm đáng kể. Loss of value không xuất hiện như monthly transfer nhưng làm net worth giảm.

Mental model:

```text
Cash affordability
≠ economic affordability
```

Một household có thể trả payment mỗi tháng nhưng vẫn đang chuyển quá nhiều wealth vào depreciating asset.

## 4. Down payment và liquidity

Giả sử cần 10m KRW down payment. Nếu household có 18m KRW liquid savings, transaction làm cash còn 8m.

Nếu essential burn là 2.5m/tháng:

```text
Before car: 18 / 2.5 = 7.2 months
After down payment: 8 / new burn
```

Sau khi mua xe, burn cũng tăng. Nếu new essential-ish burn là 3.4m:

```text
8 / 3.4 ≈ 2.35 months
```

Transaction có thể làm resilience giảm từ hơn 7 tháng xuống gần 2 tháng dù salary cao hơn.

## 5. Car loan tạo fixed obligation

Một discretionary purchase được finance bằng debt biến thành contractual payment.

Điều này quan trọng vì:

```text
income can fall
but required payment remains
```

Khi household mất job, loan payment cạnh tranh trực tiếp với rent, food và emergency cash.

Đây là lý do fixed-cost load phải được stress-test ở [15 Financial Resilience](../15-financial-resilience.md).

## 6. Income rise dễ bị lifestyle inflation hấp thụ

Trước raise:

```text
Income 3.8m
Spending 3.0m
Saving margin 0.8m
```

Sau raise và car:

```text
Income 5.0m
Old spending 3.0m
Car cash cost 1.25m
Saving margin 0.75m
```

Thu nhập tăng 31.6%, nhưng saving margin lại giảm.

Household cảm thấy “kiếm nhiều hơn” nhưng wealth-building capacity không tăng.

## 7. Compare với mobility service cần mua

Câu hỏi first-principles:

```text
What problem does the car solve?
```

Có thể là:

- commute quá dài;
- shift work không có public transport;
- family/child transport;
- frequent intercity travel;
- equipment transport;
- convenience/lifestyle.

Nếu car giúp tăng earning capacity hoặc tiết kiệm rất nhiều time, benefit thực có thể lớn. Nhưng benefit phải được mô tả rõ, không mặc định “car = necessity”.

## 8. Used vs new không chỉ là purchase price

Used car có thể giảm initial depreciation nhưng tăng uncertainty về repair/maintenance. New car có warranty/operational predictability nhưng initial value loss cao hơn.

Decision variables:

```text
purchase price
expected holding period
repair probability
maintenance cost
insurance
financing terms
resale value uncertainty
reliability requirement
```

Không có một rule universal “used luôn tốt hơn”.

## 9. Stress test

### Scenario A — income giảm 20%

```text
Income 5.0m → 4.0m
Car cost remains ~1.25m
```

Nếu old lifestyle cost không giảm, saving margin gần biến mất.

### Scenario B — repair 2m KRW ngay sau purchase

Nếu down payment đã làm emergency fund mỏng, repair có thể đẩy household vào credit-card debt.

### Scenario C — muốn chuyển việc/thành phố

Car loan và resale friction làm mobility decision phức tạp hơn.

### Scenario D — parking/insurance/fuel cost tăng

Operating cost inflation có thể làm TCO cao hơn estimate ban đầu.

## 10. Affordability gate

Một car purchase nên được đánh giá sau transaction:

```text
Emergency fund months = ?
Fixed-cost ratio = ?
Debt service ratio = ?
Monthly saving margin = ?
Known future goals still funded = ?
Can household survive 3–6 month income shock without selling car or borrowing more = ?
```

Không dùng dealer-approved loan amount làm affordability metric. Lender underwriting và household resilience là hai câu hỏi khác nhau.

## Kết luận

Salary increase không tự động biến mọi lifestyle upgrade thành affordable. Car là một package gồm **depreciating asset + operating expenses + possible debt + reduced liquidity**.

Câu hỏi quan trọng nhất không phải “monthly payment bao nhiêu?” mà là: **sau khi mua, household còn bao nhiêu margin để chịu shock và tài trợ các mục tiêu khác?**

Đọc [10 Car Finance](../10-car-finance.md), [12 Emergency Fund](../12-emergency-fund.md), [14 Personal Balance Sheet](../14-personal-balance-sheet.md) và [15 Financial Resilience](../15-financial-resilience.md).