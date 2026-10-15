# 19 — Annual Financial Review: kiểm tra lại toàn bộ hệ thống mỗi năm

## Định vị

Personal Finance không kết thúc ở việc đọc xong chapter hoặc lập một budget một lần. Household thay đổi liên tục:

```text
income thay đổi
family thay đổi
housing thay đổi
rates/prices thay đổi
debt giảm hoặc tăng
insurance coverage cũ đi
accounts proliferate
goals và country/residency thay đổi
```

Vì vậy cần một **annual financial review (연간 재무 점검)**: một lần mỗi năm nhìn toàn bộ household như một system thay vì kiểm tra từng sản phẩm riêng lẻ.

Review này không nhằm tối ưu từng đồng. Mục tiêu là phát hiện:

```text
hidden fragility
stale assumptions
unnecessary complexity
coverage gaps
liquidity gaps
new concentration
cross-border mismatch
```

## 1. Snapshot trước khi phân tích

Bắt đầu bằng một snapshot ngày review:

```text
review date
household members/dependents
country/residency context
monthly take-home income
essential monthly spending
liquid assets
long-term assets
debt balance + payment
insurance coverage map
housing structure
retirement resources
major obligations in next 12–24 months
```

Không cần precision kiểu audit kế toán. Cần đủ nhất quán để so với năm trước.

## 2. Cash-flow review

Từ [01 — Money](./01-money.md), trả lời:

```text
Income có tăng hay giảm?
Essential spending tăng do inflation hay lifestyle?
Fixed cost nào mới xuất hiện?
Savings margin có tốt hơn hay xấu hơn?
Có annual/irregular expense nào bị bỏ ngoài monthly budget?
```

Một signal quan trọng:

```text
income ↑
but
savings margin ↔ or ↓
```

Điều này thường nghĩa lifestyle/fixed obligations đang hấp thụ income growth.

### Rebuild three numbers

```text
normal monthly burn
emergency monthly burn
monthly investable surplus
```

Ba số này phục vụ ba decision khác nhau và không nên dùng lẫn.

## 3. Liquidity review

Từ [12 — Emergency Fund](./12-emergency-fund.md) và [15 — Financial Resilience](./15-financial-resilience.md):

```text
liquid runway = liquid emergency resources / emergency monthly burn
```

Sau đó hỏi:

```text
Runway có giảm do spending tăng không?
Có khoản cash nào thực ra đã earmark cho house/car/tax/travel không?
Emergency money có accessible nhanh không?
Nếu main bank account bị khóa, household còn payment rail khác không?
```

Một account có balance cao nhưng bị locked hoặc earmarked không nên được tính hoàn toàn như emergency liquidity.

## 4. Debt review

Từ [05 — Credit](./05-credit.md) và [06 — Loans & Debt](./06-loans-debt.md), lập lại debt map:

```text
balance
interest structure
minimum/required payment
maturity
secured/unsecured
fixed/variable/reset
prepayment/refinance constraints
```

Review không chỉ hỏi debt balance đã giảm bao nhiêu. Hỏi:

```text
monthly debt service có chiếm nhiều income hơn không?
rate-reset risk có tăng không?
new debt có được tạo để finance consumption không?
liquidity có bị dùng hết để trả debt quá nhanh không?
```

Nếu household vừa có debt vừa invest, xem lại logic trong [Case 04 — Debt vs Investing](./case-studies/04-debt-vs-investing.md).

## 5. Insurance review

Từ [07 — Insurance](./07-insurance.md):

```text
What loss would materially damage household now?
```

Life event có thể làm coverage cũ không còn phù hợp:

```text
marriage
child
new home
new debt
higher income
new dependent
move country
self-employment
```

Review:

```text
insured person
coverage purpose
coverage amount conceptually sufficient?
deductible/exclusion understood?
beneficiary/contact info current?
claim process known?
```

Không bắt đầu bằng việc mua thêm policy. Bắt đầu bằng exposure map.

## 6. Housing and car review

Từ [09 — Housing](./09-housing.md) và [10 — Car Finance](./10-car-finance.md), kiểm tra total cost chứ không chỉ monthly payment.

Housing:

```text
rent/mortgage
maintenance
fees/tax/insurance
capital locked
debt structure
expected holding period
```

Car:

```text
loan/lease payment
insurance
fuel/energy
parking/tolls
maintenance
repairs
depreciation
```

Nếu salary tăng nhưng housing/car upgrade cũng tăng mạnh, review fixed-cost load trước khi gọi income growth là wealth progress.

## 7. Retirement review

Từ [11 — Retirement](./11-retirement.md):

```text
contribution continuity
retirement account balances
pension records
future spending assumptions
inflation assumption
retirement country/currency assumption
```

Không cần dự báo chính xác retirement date mỗi năm. Cần xác định plan có bị lệch vì:

```text
contribution gap
career break
move country
new dependent
large withdrawal
asset concentration
```

Cross-border worker nên đọc thêm [Case 09 — Cross-Border Retirement](./case-studies/09-cross-border-retirement.md).

## 8. Balance-sheet review

Từ [14 — Personal Balance Sheet](./14-personal-balance-sheet.md), cập nhật:

```text
assets
- liabilities
= net worth
```

Nhưng không dừng ở net worth.

Tách assets thành:

```text
liquid
investable
use assets
restricted/locked
```

và liabilities theo:

```text
short/long term
fixed/variable rate
secured/unsecured
```

### Net-worth attribution

Hỏi net worth thay đổi vì:

```text
saving?
debt repayment?
asset-price movement?
FX movement?
one-off transfer/inheritance?
```

Nếu net worth tăng chỉ vì market price tăng còn cash-flow margin xấu đi, system không nhất thiết khỏe hơn.

## 9. Resilience stress test

Mỗi năm chạy lại ít nhất các scenario trong [15 — Financial Resilience](./15-financial-resilience.md):

```text
A. income -30% for 6 months
B. income = 0 for 3 months
C. housing/debt payment +20%
D. unexpected expense = 2 months essential burn
E. main account inaccessible for 7 days
F. foreign-currency obligation +15% in home-currency terms
```

Không cần mọi scenario đều “pass” hoàn hảo. Điều cần biết là:

```text
where does the system fail first?
```

Failure point cho biết ưu tiên sửa tiếp theo.

## 10. Fraud and account-security review

Từ [13 — Financial Scams](./13-financial-scams.md):

```text
main email secured?
MFA/recovery current?
old phone number removed?
unused financial accounts closed?
transaction alerts enabled?
family knows incident-response path?
```

Security review là một phần của financial review vì account takeover có thể tạo direct financial loss và liquidity disruption.

## 11. Cross-border review

Nếu household có nhiều country/currency, từ [17 — Cross-Border Personal Finance](./17-cross-border-personal-finance.md) kiểm tra:

```text
income currency
spending currency
debt currency
family-support currency
emergency liquidity by country
remittance route
asset transferability
residency/tax/pension assumptions
```

Đặc biệt hỏi:

> Có assumption nào năm ngoái đúng nhưng năm nay đã thay đổi vì visa, residency, employment hoặc location không?

## 12. Financial continuity review

Dùng [Case 10 — Death/Incapacity Continuity](./case-studies/10-death-incapacity-continuity.md):

```text
Nếu primary financial operator unavailable 30 ngày,
người còn lại có biết phải làm gì không?
```

Review:

```text
institution inventory
obligation map
insurance inventory
beneficiary/contact records
document location
recovery process
```

Không lưu secret thiếu an toàn chỉ để “dễ dùng”. Mục tiêu là continuity mà vẫn giữ security.

## 13. Complexity cleanup

Một annual review nên xóa complexity chứ không chỉ thêm sản phẩm.

Tìm:

```text
unused accounts
redundant cards
small forgotten balances
subscriptions
old insurance/policies
obsolete autopays
outdated contact/recovery info
duplicate savings buckets
```

Financial system càng phức tạp, operational risk và cognitive load càng lớn.

## 14. Goal review

Goals không nên chỉ là slogan như “mua nhà”, “nghỉ hưu sớm”, “đầu tư nhiều hơn”.

Biến thành:

```text
goal
amount/resource needed
time horizon
priority
currency/location
liquidity requirement
what must not be sacrificed
```

Ví dụ:

```text
Goal: down payment in 3 years
→ short horizon
→ high liquidity need
→ should not rely entirely on volatile assets
```

Mục tiêu quyết định asset suitability; không phải asset hấp dẫn quyết định mục tiêu.

## 15. Investable-surplus gate

Chỉ sau khi review cash flow, liquidity, debt và resilience mới hỏi:

```text
How much capital is truly investable?
```

Một practical definition:

```text
available cash
- near-term obligations
- emergency reserve requirement
- planned major purchases
- required debt payments/reserves
= candidate investable surplus
```

Sau gate này mới handoff sang [Investing](../investing/README.md).

## 16. Annual output: chỉ cần một trang decision log

Review không cần kết thúc bằng 50 KPI. Một output ngắn có thể là:

```text
Current state
3 strengths
3 fragilities
3 actions for next 12 months
assumptions to verify
major review triggers
```

Ví dụ:

```text
Fragility 1: emergency runway fell from 6.5 to 4.2 months
Action: rebuild reserve before increasing monthly investment

Fragility 2: housing fixed cost rose sharply
Action: stress-test one-income scenario

Fragility 3: KRW income / VND family obligation increased
Action: pre-fund next 6 months of known VND obligation gradually
```

Decision log giúp năm sau phân biệt:

```text
what changed because of deliberate action
vs
what changed because markets/life happened
```

## 17. Review trigger ngoài lịch hàng năm

Không chờ đủ một năm nếu có major event:

```text
job change/job loss
marriage/divorce
birth/death
move country
buy/sell house
large debt
large windfall/loss
health event
business/self-employment start
major tax/residency change
fraud/security incident
```

Annual review là minimum cadence, không phải maximum.

## Kết luận

Một household financial system khỏe không cần tối ưu mọi ratio. Nó cần biết trạng thái hiện tại, failure mode và next action rõ ràng.

```text
Observe
→ reconcile
→ stress-test
→ simplify
→ repair fragility
→ identify investable surplus
→ review again after life changes
```

Chapter này biến toàn bộ `personal-finance/` thành một loop thay vì một syllabus đọc xong rồi bỏ.