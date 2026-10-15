# 14 — Bảng cân đối tài chính cá nhân (Personal Balance Sheet / 개인 대차대조표)

## Định vị

Các chapter trước nhìn từng thành phần: tiền, tài khoản, lãi suất, lạm phát, tín dụng, nợ, bảo hiểm, thuế, nhà, xe, hưu trí, quỹ dự phòng và scam. Chapter này gom chúng vào hai báo cáo khái niệm: **bảng cân đối cá nhân (personal balance sheet / 개인 대차대조표)** cho biết mình sở hữu và nợ gì tại một thời điểm; **báo cáo dòng tiền cá nhân (personal cash-flow statement / 개인 현금흐름표)** cho biết tiền đi vào và ra trong một khoảng thời gian.

Mục tiêu không phải tạo accounting phức tạp mà có một dashboard đủ tốt để trả lời: hệ thống tài chính đang mạnh lên hay chỉ có thu nhập/giá tài sản tăng tạm thời? Sau khi dựng được snapshot này, [15 — Financial Resilience](./15-financial-resilience.md) sẽ stress-test nó dưới income, expense, rate, FX và operational shocks.

## Phương trình cơ bản

```text
Net worth = Assets − Liabilities
```

Tài sản (assets / 자산) là nguồn lực có giá trị kinh tế mà cá nhân sở hữu hoặc có quyền lợi. Nợ phải trả (liabilities / 부채) là nghĩa vụ với bên khác. Tài sản ròng (net worth / 순자산) là phần còn lại sau khi trừ nợ.

Ví dụ:

```text
Cash & deposits        20
Investments            30
Home                  300
Car                    15
-------------------------
Total assets          365

Mortgage              220
Car loan                8
Credit card             2
-------------------------
Total liabilities     230

Net worth             135
```

Con số 135 không có nghĩa có 135 cash. Phần lớn có thể bị khóa trong home equity. Vì thế net worth phải đi cùng liquidity analysis.

## Asset classification theo chức năng

Một bảng tốt không chỉ liệt kê value; nên phân loại theo khả năng sử dụng.

### Liquid assets

Tài sản thanh khoản (liquid assets / 유동자산) có thể chuyển thành tiền dùng cho nghĩa vụ gần với chi phí/biến động thấp: cash, transaction deposits và một số savings.

### Investable assets

Tài sản đầu tư (investable assets / 투자자산) dành cho mục tiêu dài hơn và có thể chịu market risk. Chi tiết classification thuộc [Investing](../investing/README.md).

### Use assets

Tài sản phục vụ sử dụng (use assets / 사용자산) như primary home hoặc car cung cấp dịch vụ đời sống. Chúng có value nhưng không nhất thiết tạo cash flow và có thể tốn maintenance.

### Restricted/retirement assets

Tài sản bị hạn chế hoặc dành cho hưu trí có thể có withdrawal rules, tax và penalty. Balance trước tax không nên được xem như cash tương đương.

Phân loại này ngăn lỗi “net worth cao nên không cần emergency fund”. Một household có home equity lớn nhưng cash gần 0 vẫn dễ bị stress.

## Liability classification

Nợ nên được ghi ít nhất với:

```text
balance
interest rate
minimum/required payment
maturity
fixed/variable
secured/unsecured
collateral
```

Tổng liabilities cho biết leverage, còn payment schedule cho biết cash-flow pressure. Hai household cùng nợ 100 nhưng một người có loan 2% dài hạn, người kia có revolving debt 20% là hai cấu trúc khác hẳn.

## Liquid net worth

Tài sản ròng thanh khoản (liquid net worth / 유동순자산) nhằm trả lời: nếu cần nguồn lực nhanh mà không bán home/car, còn bao nhiêu?

Một định nghĩa thực hành có thể là:

```text
Liquid net worth
= liquid assets + readily saleable financial assets
− short-term / callable liabilities
```

Không có definition duy nhất. Quan trọng là ghi rule nhất quán. Nếu investment có volatility cao, có thể stress-test value thay vì dùng market value hiện tại 100%.

## Cash flow nối balance sheet qua thời gian

Net worth là snapshot. Dòng tiền (cash flow / 현금흐름) giải thích chuyển động giữa hai snapshot.

Ví dụ trả 1 mortgage payment 1,500 không phải toàn bộ làm net worth giảm 1,500. Một phần là interest expense, một phần giảm principal và tăng home equity tương ứng nếu home value không đổi.

Tương tự, chuyển 500 từ checking sang investment không phải expense theo nghĩa giảm net worth; đó là asset reallocation. Ngược lại, depreciation của car làm asset value giảm dù không có cash outflow cùng tháng.

Do đó cần tránh đồng nhất:

```text
cash outflow ≠ expense in every case
cash inflow ≠ income in every case
asset purchase ≠ wealth creation automatically
loan proceeds ≠ income
```

Đây là điểm mạnh nhất của balance-sheet thinking.

## Theo dõi net worth mà không bị market noise điều khiển

Cập nhật quá thường xuyên có thể khiến biến động market hoặc FX che mất trend thực. Với personal finance, monthly hoặc quarterly thường đủ cho nhiều người, trong khi tax/retirement audit có thể làm annual review sâu hơn.

Khi net worth tăng, phân rã nguyên nhân:

```text
saving from income
+ investment return
+ asset revaluation
− interest/fees/taxes
− depreciation/consumption
= change in net worth
```

Nếu net worth chỉ tăng vì house/stock valuation nhưng savings rate âm và debt tăng, resilience có thể không cải thiện.

## Các tỷ lệ hữu ích

### Savings rate

Có thể định nghĩa:

```text
Savings rate = amount saved / relevant after-tax income
```

Nhưng phải thống nhất “saved” bao gồm retirement contributions, principal repayment hay không. Mục tiêu là trend, không phải tranh luận một definition universal.

### Debt service ratio

```text
Debt service ratio = required debt payments / income
```

Cho biết bao nhiêu cash flow bị khóa vào nghĩa vụ nợ. Nó bổ sung cho DTI ở [06 — Loans & Debt](./06-loans-debt.md).

### Emergency coverage

```text
Emergency coverage months = liquid emergency resources / essential monthly burn
```

Nối trực tiếp với [12 — Emergency Fund](./12-emergency-fund.md).

### Leverage

```text
Leverage = total assets / net worth
```

Khi net worth nhỏ so với assets, biến động asset value có thể khuếch đại mạnh vào equity. Ratio này cần đọc cùng asset type; home mortgage khác margin borrowing.

## Personal finance dashboard tối giản

Một dashboard có thể chỉ cần:

```text
Monthly take-home income
Essential spending
Discretionary spending
Debt payments
Emergency-fund months
Total assets
Total liabilities
Net worth
Liquid net worth
Retirement contributions
Insurance coverage gaps / renewal dates
Major upcoming sinking-fund needs
```

Mục tiêu là biến financial life thành một system có trạng thái quan sát được. Không cần 50 KPI nếu không dẫn đến decision.

## Decision journal cho quyết định lớn

Với home, car, refinancing hoặc insurance, lưu một note trước quyết định:

```text
What problem am I solving?
What assumptions must be true?
What happens to monthly cash flow?
What happens to liquid net worth?
What debt/risk is added?
What would make me reverse/review this decision?
```

Sau 6–12 tháng, review assumptions. Cách này tách outcome may mắn khỏi decision quality.

## Financial health không phải net worth ranking

Net worth hữu ích để theo dõi chính mình qua thời gian, nhưng không nên biến thành bảng xếp hạng giữa người có hoàn cảnh khác nhau. Tuổi, country, pension system, family size, housing system và income trajectory làm balance sheet khác biệt.

Mục tiêu của personal finance là **khả năng đáp ứng nghĩa vụ, hấp thụ shock và tài trợ mục tiêu**, không phải tối đa hóa một con số duy nhất bằng mọi giá.

## Từ balance sheet sang resilience rồi mới sang Investing

Phần core có thể rút về một chuỗi:

```text
Income
→ cash flow
→ liquidity
→ debt & insurance
→ taxes and major life assets
→ emergency resources
→ long-term retirement resources
→ balance sheet
→ resilience stress test
→ investable surplus
```

Balance sheet trả lời **mình đang đứng ở đâu**. Nó chưa trả lời cấu trúc đó có sống sót khi income giảm, rate tăng, FX đi bất lợi hoặc account bị gián đoạn hay không. Vì vậy bước tiếp theo là [15 — Financial Resilience](./15-financial-resilience.md).

Sau resilience gate, [Economics](../economics/README.md) giúp hiểu môi trường lãi suất, inflation, growth và policy; [Investing](../investing/README.md) giúp quyết định asset allocation, security analysis và risk/return. Forex nằm ở [`investing/05_trading_derivatives/forex/`](../investing/05_trading_derivatives/forex/README.md); cổ phiếu và các asset classes nằm trong [`investing/02_asset_classes/`](../investing/02_asset_classes/README.md).

Điểm bàn giao của chapter này vì vậy không phải “net worth cao thì hãy đầu tư”, mà là: **đã có đủ dữ liệu để kiểm tra phần vốn nào vẫn tồn tại như investable surplus sau khi household chịu stress hay chưa**.
