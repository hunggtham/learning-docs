# Case 01 — Mất việc sáu tháng: hệ thống tài chính chịu shock ra sao?

## Bối cảnh

Một người có thu nhập take-home 4.2 triệu KRW/tháng. Chi phí bình thường khoảng 3.0 triệu KRW/tháng, trong đó 2.1 triệu là chi phí thiết yếu. Người này có 14 triệu KRW cash/savings, 18 triệu KRW investment, không có mortgage nhưng có car loan còn 8 triệu KRW với payment 450 nghìn KRW/tháng.

Đột ngột mất việc và chưa biết khi nào có income mới. Case này không hỏi “có nên bán investment không?” ngay từ đầu. Câu hỏi đúng hơn là: **household có bao nhiêu thời gian để phục hồi trước khi buộc phải vay, bán tài sản hoặc phá vỡ kế hoạch dài hạn?**

## 1. Tách cash flow thành ba lớp

Không nên lấy spending bình thường làm burn rate khẩn cấp. Trước tiên tách:

```text
Normal spending           3.0m
Essential spending        2.1m
Debt payment              0.45m
Discretionary / deferrable 0.45m
```

Trong shock, household có thể giảm một phần discretionary spending. Nhưng car loan là fixed obligation; rent, utilities, food, insurance và nghĩa vụ gia đình thiết yếu cũng không biến mất.

Một emergency burn hợp lý để stress-test có thể là:

```text
Essential living  2.1m
Debt payment      0.45m
-----------------------
Emergency burn    2.55m KRW/month
```

Đây chỉ là số minh họa. Mục tiêu là hiểu cơ chế: **burn rate phải phản ánh cash outflow khó trì hoãn**, không phải toàn bộ lifestyle trước shock.

## 2. Liquidity runway

Với 14 triệu KRW cash/savings:

```text
Runway = liquid emergency resources / emergency monthly burn
        = 14 / 2.55
        ≈ 5.5 months
```

Điều này không có nghĩa “an toàn 5.5 tháng”. Một số chi phí lớn có thể phát sinh trước đó: chuyển nhà, deductible, sửa xe, visa/work transition, family emergency.

Vì vậy nên coi 5.5 tháng là **maximum static runway under assumptions**, sau đó stress-test.

## 3. Stress test nhiều recovery time

### Scenario A — có việc mới sau 2 tháng

Cash burn khoảng 5.1 triệu KRW trước khi income phục hồi. Household còn đủ liquidity để tránh bán investment trong điều kiện bình thường.

### Scenario B — có việc mới sau 5 tháng

Cash burn khoảng 12.75 triệu KRW. Buffer gần chạm đáy. Nếu job mới còn delay payroll một tháng, hệ thống có thể thiếu cash dù về lý thuyết đã “có việc”.

### Scenario C — 8 tháng chưa có việc

Cash-only buffer không đủ. Household cần quyết định trước khi tháng thứ 5 đến, thay vì chờ cash gần bằng 0 rồi mới phản ứng.

Mental model:

```text
shock starts
→ measure runway
→ reduce burn
→ protect insurance / housing / legal status
→ improve income recovery probability
→ prepare secondary liquidity
→ only then consider forced asset sale / new debt
```

## 4. Investment không tự động là emergency fund

18 triệu KRW investment làm net worth tốt hơn, nhưng không phải toàn bộ là emergency liquidity.

Nếu market giảm đúng lúc mất việc, bán asset có thể biến temporary drawdown thành permanent loss. Nếu asset cần settlement/transfer hoặc nằm ở tài khoản bị hạn chế, access time cũng khác cash.

Do đó cần tách:

```text
Net worth ≠ liquidity
Market value ≠ immediately usable cash
```

Có thể lập secondary liquidity plan, nhưng không nên giả định investment = cash 1:1.

## 5. Có nên trả hết car loan ngay để giảm monthly payment?

Giả sử dùng phần lớn 14 triệu cash để trả 8 triệu car loan. Monthly obligation giảm 450 nghìn KRW, nhưng liquidity lập tức giảm mạnh.

Trước payoff:

```text
Cash = 14m
Burn = 2.55m
Runway ≈ 5.5 months
```

Sau payoff, giả sử cash còn 6m và burn giảm còn 2.1m:

```text
Runway = 6 / 2.1
       ≈ 2.9 months
```

Dù balance sheet có ít debt hơn, resilience có thể xấu đi vì cash bị khóa vào một quyết định không dễ đảo ngược.

Đây là ví dụ điển hình cho việc **solvency improvement không luôn đồng nghĩa liquidity improvement**.

## 6. Expense triage

Thay vì cắt ngẫu nhiên, chia expense thành:

```text
Tier A — must preserve
housing, food, utilities, insurance, minimum debt, legal/visa-related cost

Tier B — useful for recovery
phone, internet, transport, job-search cost, training cần thiết

Tier C — deferrable
subscriptions, leisure, upgrades, discretionary shopping
```

Một lỗi phổ biến là cắt cả Tier B quá mạnh, làm giảm khả năng tìm việc và kéo dài shock.

## 7. Income recovery là một phần của financial plan

Trong unemployment shock, mục tiêu không chỉ là giảm expense. Cần tăng xác suất phục hồi income:

```text
update CV / portfolio
→ activate network
→ widen acceptable roles temporarily
→ use eligible public/employment support if applicable
→ protect work/visa status if relevant
→ define minimum acceptable bridge income
```

Chi tiết quyền lợi lao động, unemployment insurance hoặc visa tại Hàn Quốc thuộc canonical owner [Korea Law, Civic & Everyday Life](../../korea_law_civic_life/README.md), không hard-code trong case này.

## 8. Trigger thay vì chờ cảm giác

Nên định nghĩa trước các trigger:

```text
If runway < 4 months
→ freeze discretionary commitments

If runway < 3 months
→ activate secondary liquidity plan

If runway < 2 months
→ reassess housing/car/debt structure urgently
```

Con số exact không universal. Giá trị của trigger là tránh decision paralysis khi stress tăng.

## 9. Khi nào mới quay lại Investing?

Sau khi có việc mới, không nhất thiết lập tức đưa mọi cash còn lại vào market. Household cần rebuild resilience:

```text
income stabilized
→ overdue obligations cleared
→ emergency floor rebuilt
→ insurance / tax / housing gaps checked
→ high-cost debt reassessed
→ investable surplus re-established
```

Chỉ phần vốn vượt resilience floor mới nên được coi là investable surplus.

## Kết luận

Bài học của case không phải “giữ X tháng emergency fund”. Nó là:

**mất việc là một cash-flow shock có duration không chắc chắn; household cần quản lý runway, fixed obligations, recovery capacity và secondary liquidity như một hệ thống.**

Đọc lại [12 — Emergency Fund](../12-emergency-fund.md), [14 — Personal Balance Sheet](../14-personal-balance-sheet.md) và [15 — Financial Resilience](../15-financial-resilience.md) để nối case về framework gốc.