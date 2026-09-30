# Case 04 — Trả nợ hay đầu tư? So guaranteed saving với expected return

## Bối cảnh

Một household có 20 triệu KRW cash ngoài emergency floor tối thiểu. Đồng thời còn một khoản debt 20 triệu KRW với lãi suất 7%/năm. Người này cân nhắc hai lựa chọn:

```text
A. trả hết debt
B. giữ debt và đầu tư 20m KRW vào portfolio rủi ro
```

Case không đưa verdict universal. Câu hỏi đúng là: **sự khác biệt giữa return chắc chắn từ debt payoff và expected return không chắc chắn từ investing thay đổi household risk như thế nào?**

## 1. Debt payoff tạo một saving gần như chắc chắn

Nếu debt thật sự có cost 7% và không có penalty/benefit đặc biệt làm thay đổi bài toán, trả nợ giảm future interest expense.

Mental model:

```text
Paying off 7% debt
≈ earning a guaranteed 7% pre-tax equivalent saving
```

Đây không phải investment return theo nghĩa market asset, nhưng từ household cash flow, cost avoided là measurable benefit.

## 2. Expected return không phải guaranteed return

Giả sử một risky portfolio có long-run expected return cao hơn 7%. Điều đó không có nghĩa next 1–3 years sẽ cao hơn 7%.

Có thể xảy ra:

```text
Year 1 market return = -25%
Debt cost = +7%
```

Household chịu cả asset loss lẫn fixed debt obligation. Vì vậy so sánh phải dùng:

```text
guaranteed debt cost
vs
uncertain distribution of investment outcomes
```

Không dùng single expected-return number như certainty.

## 3. Liquidity làm bài toán thay đổi

Nếu 20m KRW là toàn bộ liquid cash ngoài checking, trả hết debt có thể làm liquidity quá thấp.

Ví dụ:

```text
Before payoff
Cash outside emergency floor = 20m
Debt = 20m

After payoff
Cash outside floor = 0
Debt = 0
```

Balance sheet leverage cải thiện, nhưng optionality giảm. Nếu emergency floor bản thân quá thấp hoặc sắp có large expense, full payoff có thể làm resilience xấu đi.

Do đó thứ tự thường phải là:

```text
protect minimum liquidity
→ assess debt cost/risk
→ determine investable surplus
→ allocate remaining capital
```

## 4. Tax và product structure có thể làm comparison khác

Debt interest có thể có tax treatment khác nhau theo jurisdiction/product. Investment gain cũng có tax treatment riêng.

Không nên dùng raw rate nếu tax materially affects outcome.

Framework:

```text
Effective debt cost after relevant tax effects
vs
Expected investment return after fees/taxes
```

Rule cụ thể phải kiểm tra theo jurisdiction và thời điểm.

## 5. Fixed-rate debt khác variable-rate debt

Một fixed 2% loan và variable 9% debt không nên nằm cùng một category chỉ vì đều là debt.

Debt analysis phải nhìn:

```text
rate
fixed / variable
maturity
payment burden
prepayment terms
collateral
refinance risk
```

Variable debt còn thêm rate shock. Khi rate tăng, household cash flow có thể xấu mà portfolio return chưa kịp bù.

## 6. High-cost revolving debt tạo asymmetry mạnh

Với revolving credit cost cao, bar cho “đầu tư thay vì trả nợ” trở nên rất cao vì:

- debt cost chắc chắn;
- investment return không chắc chắn;
- payment/late-fee/credit consequences có thể lớn;
- household dễ forced-sell investment khi cash flow stress.

Case này cho thấy investment decision không thể tách khỏi liability side của balance sheet.

## 7. Partial strategy

Không nhất thiết lựa chọn 100% A hoặc 100% B.

Có thể có structure:

```text
20m available
→ 8m preserve/reinforce liquidity
→ 8m debt reduction
→ 4m long-horizon investing
```

Con số chỉ minh họa. Giá trị của partial strategy là giảm binary thinking và nhìn capital allocation ở cấp household.

## 8. Stress test bốn kịch bản

### Scenario A — income stable, market strong

Investing while carrying debt có thể tạo higher realized wealth nếu return thực tế vượt debt cost đủ nhiều.

### Scenario B — income stable, market weak

Debt vẫn phải trả; portfolio có thể drawdown. Household phải chịu volatility nhưng có income support.

### Scenario C — mất việc, market weak cùng lúc

Đây là critical scenario vì labor income và risky asset thường có thể cùng xấu trong recession. Nếu household cần bán asset để service debt, risk compounding xuất hiện.

### Scenario D — rate tăng trên variable debt

Debt cost tăng trong khi expected portfolio return không tự động tăng. Cash-flow margin thu hẹp.

Stress test phải ưu tiên Scenario C/D hơn việc chỉ so expected value bình thường.

## 9. Resilience gate trước investing

Một amount chỉ nên được gọi là investable surplus nếu:

```text
emergency floor vẫn đủ
+ near-term known expenses đã funded
+ required debt payments chịu được stress
+ không cần asset này để trả nghĩa vụ 1–3 năm gần
+ household chấp nhận drawdown mà không forced sell
```

Nếu không, capital đó vẫn thuộc personal-finance buffer, chưa phải investment capital.

## 10. Decision journal

Trước khi quyết định, ghi:

```text
Debt effective cost = ?
Fixed or variable = ?
Emergency months after decision = ?
Known expenses next 24 months = ?
Investment horizon = ?
Maximum drawdown household can tolerate without selling = ?
What event would make me reverse the plan = ?
```

Sau 12 tháng, review reasoning thay vì chỉ nhìn outcome. Một investment lãi mạnh không chứng minh initial decision luôn tốt nếu household đã nhận risk không cần thiết.

## Kết luận

“Trả nợ hay đầu tư?” không phải một câu hỏi investment thuần túy. Nó là **capital allocation problem trên toàn balance sheet**.

Debt payoff cho cost saving có độ chắc chắn cao; investing cho expected return nhưng đi cùng uncertainty. Liquidity, fixed obligations và downside quyết định phần vốn nào thực sự có thể chịu market risk.

Đọc [06 Loans & Debt](../06-loans-debt.md), [14 Personal Balance Sheet](../14-personal-balance-sheet.md) và [15 Financial Resilience](../15-financial-resilience.md).