# Shinhan Financial Group — ngân hàng, holding company, credit cycle và capital adequacy

Case này dùng Shinhan Financial Group như một laboratory để hiểu **financial holding company (금융지주회사)** của Hàn Quốc. Mục tiêu không phải đánh giá Shinhan tốt hay xấu, mà học cách đọc một tập đoàn tài chính khác hoàn toàn một manufacturer.

Với manufacturer, ta thường bắt đầu từ volume, price, cost, CAPEX và free cash flow. Với bank, tiền vừa là phương tiện thanh toán vừa gần với “raw material” của business. Deposit, wholesale funding, loans, securities, credit losses và regulatory capital tạo thành một balance-sheet engine. Vì vậy nếu áp dụng máy móc `Revenue - Cost - CAPEX = FCF` của công ty công nghiệp, mental model sẽ sai ngay từ đầu.

Xem nền tảng tại [35_financial_sector_securities_insurance_asset_management](../35_financial_sector_securities_insurance_asset_management.md), [11_banks_finance_and_corporate_funding](../11_banks_finance_and_corporate_funding.md) và [01_macro_economy_and_business_cycle](../01_macro_economy_and_business_cycle.md).

## 1. Entity resolution: Shinhan Financial Group không đồng nghĩa Shinhan Bank

Một **financial holding company (금융지주회사)** sở hữu nhiều financial subsidiaries. Commercial bank có thể là cash engine lớn nhất, nhưng group còn có card, securities, insurance, asset-management và các financial businesses khác.

Điểm quan trọng là mỗi subsidiary có economics và regulation riêng. Bank bị chi phối bởi deposit funding, loan quality và bank capital. Securities company nhạy với brokerage, investment banking, trading và market liquidity. Card business nhạy với consumer credit, funding cost và delinquency. Insurance cần đọc liabilities, investment portfolio và solvency theo logic riêng.

Do đó câu “Shinhan earnings tăng” mới chỉ là observation. Analyst phải hỏi **subsidiary nào tạo ra thay đổi, bằng driver nào và sử dụng bao nhiêu capital để tạo ra return đó**.

> **Mental Model:** financial group là một portfolio của nhiều balance-sheet businesses. Consolidated earnings chỉ là kết quả cuối; analysis phải quay ngược về asset quality, funding, spread, fee và regulatory capital của từng engine.

## 2. Bank thực sự kiếm tiền như thế nào?

Một simplified banking engine có thể viết:

```text
Deposits + wholesale funding + equity
                ↓
      loans + securities + liquidity assets
                ↓
 interest income - interest expense
                ↓
       Net interest income
                +
       fees / other income
                -
 operating cost + credit loss
                ↓
              profit
```

### Net Interest Margin — 순이자마진

**Biên lãi ròng (Net Interest Margin, NIM / 순이자마진)** mô tả spread mà bank tạo được giữa yield của interest-earning assets và funding cost, sau khi xét cấu trúc balance sheet.

Một intuition đơn giản:

\[
Net\ Interest\ Income \approx Interest\ Earning\ Assets \times NIM
\]

Nhưng NIM không chỉ là `loan rate - deposit rate`. Asset mix, deposit mix, repricing speed, fixed/floating-rate structure và competition đều ảnh hưởng.

Nếu policy rate tăng, loan yield có thể repricing nhanh trước deposit cost, khiến NIM ban đầu tăng. Nhưng sau đó deposit competition làm funding cost tăng, borrower stress làm credit cost tăng và loan demand giảm. Vì vậy “rate tăng tốt cho bank” chỉ đúng trong một số phase của transmission mechanism.

## 3. Deposit franchise là một economic moat kiểu khác

Manufacturing moat có thể là technology, scale hoặc brand. Bank moat có thể nằm ở **deposit franchise (예금 기반)**: khả năng huy động funding tương đối ổn định với cost hợp lý.

Một bank có large low-cost transaction deposits có thể fund assets rẻ hơn bank phụ thuộc nhiều vào wholesale funding. Nhưng deposit không miễn phí. Khi rate cao hoặc customers dễ chuyển sang term deposits/money-market products, deposit beta tăng và margin bị ép.

**Deposit beta** có thể hiểu là mức độ deposit rate tăng theo market/policy rate. Nếu policy rate tăng 100bp nhưng average deposit cost tăng 60bp, deposit beta theo stylized calculation là khoảng 60%.

Điều này nối trực tiếp macro policy với bank profitability.

## 4. Loan growth không đồng nghĩa value creation

Loan book tăng nhanh có thể làm net interest income tăng, nhưng growth chỉ tạo value nếu pricing bù đủ cho:

```text
Funding cost
+ operating cost
+ expected credit loss
+ unexpected risk / capital consumption
+ required return on equity
```

Nếu bank giành market share bằng cách underprice risk, accounting profit có thể đẹp trước khi losses xuất hiện.

Đây là lý do banking analysis phải luôn ghép **growth với underwriting quality**.

## 5. Credit cycle — tín dụng xấu thường đến sau tăng trưởng

**Credit cost (대손비용)** là chi phí liên quan đến expected losses và provisions. Credit deterioration thường có lag.

Causal chain có thể là:

```text
Low rates / strong economy
→ loan growth
→ leverage increases
→ rate shock / income shock
→ debt-service burden rises
→ delinquency increases
→ staging / provisions increase
→ write-offs / losses
```

Do lag này, bank có thể report strong current earnings ngay khi future risk đang được build trong balance sheet.

Khi đọc DART, không chỉ xem total loans. Cần phân tách household, mortgage, unsecured consumer, SME, large corporate, real-estate/PF và overseas exposures khi disclosure cho phép.

## 6. Household debt và housing là Korean-specific transmission channel quan trọng

Korea có household leverage và housing-finance channel quan trọng. Mortgage quality phụ thuộc không chỉ house price mà còn borrower income, LTV, DSR, interest burden và employment.

Nếu house price giảm nhưng borrower vẫn có strong cash flow và low LTV, loss có thể hạn chế. Ngược lại, collateral price ổn định không cứu được borrower thiếu cash flow mãi mãi.

Do đó:

> Collateral là secondary repayment source; income/cash flow là primary repayment source.

Policy như LTV/DSR regulation tác động đồng thời tới loan growth, household demand và financial stability. Đây là connection giữa [22_tax_regulation_and_competition](../22_tax_regulation_and_competition.md), [27_demographics_households_and_consumption](../27_demographics_households_and_consumption.md) và bank earnings.

## 7. SME và corporate lending: đọc borrower economy phía sau bank

Một bank không chỉ là financial company; loan book là một compressed map của real economy.

Nếu SME borrowers tập trung ở construction, restaurants hoặc export suppliers, macro shock ở các sectors đó có thể đi vào bank qua delinquency/provision.

Corporate credit analysis vì vậy đi hai chiều:

```text
Macro → borrower → bank asset quality
Bank lending standards → borrower funding → investment/employment → macro
```

Bank vừa nhận shock từ economy vừa truyền shock trở lại economy.

## 8. Non-interest income không phải một loại duy nhất

Fee income từ cards, brokerage, asset management hoặc wealth management có thể diversify revenue. Nhưng trading gains, valuation gains và one-off disposal gains không có cùng persistence.

Analyst nên hỏi:

```text
Recurring fee?
Market-sensitive fee?
Trading / valuation?
One-off gain?
Insurance service result?
```

Một group có diversified subsidiaries có thể giảm phụ thuộc vào NIM, nhưng diversification cũng tăng complexity và regulatory-capital allocation problem.

## 9. Cost-to-income và operating leverage

Bank có branch network, IT systems, cybersecurity, compliance, employees và digital infrastructure. **Cost-to-income ratio (영업효율성 지표)** cho thấy phần operating income bị tiêu bởi operating expenses.

Digitalization có thể giảm transaction cost nhưng đồng thời tăng technology investment. Vì vậy đóng branch không tự động đồng nghĩa sustainable cost advantage; cần xem customer acquisition, digital engagement, fraud/cybersecurity cost và legacy-system burden.

## 10. Capital adequacy — lợi nhuận phải được đặt cạnh capital

Bank không thể leverage vô hạn. Regulatory framework yêu cầu capital buffer chống losses.

**CET1 ratio (보통주자본비율)** simplified:

\[
CET1\ Ratio = \frac{Common\ Equity\ Tier\ 1}{Risk\ Weighted\ Assets}
\]

Điểm cốt lõi là denominator không phải total assets mà **risk-weighted assets (RWA / 위험가중자산)**. Hai assets cùng 100 won có thể consume regulatory capital khác nhau tùy risk weight.

Do đó ROE cao có thể đến từ genuine franchise strength, nhưng cũng có thể đến từ high leverage hoặc low capital buffer. Analyst phải nhìn return và resilience cùng nhau.

## 11. Capital allocation ở financial holding company

Holding company phải quyết định capital nên ở đâu:

```text
Retain at bank for growth / buffer
→ dividend upstream to holding
→ inject into securities/card/insurance subsidiary
→ acquisition
→ shareholder distribution
```

Một subsidiary có accounting profit cao nhưng consume rất nhiều capital chưa chắc tạo superior economic value.

Mental model phù hợp là:

\[
Economic\ Value\ Creation \approx Return\ on\ Capital - Cost\ of\ Capital
\]

với constraint regulatory capital riêng cho từng financial business.

## 12. Stress test một financial group

Một stress test không nên chỉ giảm revenue 10%. Hãy stress đúng balance-sheet mechanics.

Stylized scenario:

```text
Policy / market rates remain high
→ deposit cost rises
→ NIM compresses 15bp
→ loan growth slows
→ SME/PF delinquency rises
→ credit cost +30bp
→ securities fee income weakens
→ RWA still grows modestly
→ CET1 buffer tightens
```

Sau đó trace:

```text
NIM → net interest income
Credit cost → net income
RWA → capital ratio
Lower earnings → retained capital
Capital ratio → growth / dividend capacity
```

Đây mới là bank stress test có causal coherence.

## 13. ROE và P/B: tại sao bank thường được đọc bằng book value

Book value có ý nghĩa đặc biệt với financial company vì assets/liabilities tài chính chiếm phần lớn balance sheet và regulatory capital liên hệ trực tiếp equity.

Một intuition phổ biến:

```text
Higher sustainable ROE relative to cost of equity
→ book value economically more productive
→ market may justify higher P/B
```

Nhưng không được dùng P/B như rule máy móc. Nếu reported book value chứa asset-quality problem chưa được recognized hoặc ROE dựa vào unsustainable credit cycle, apparent cheap P/B có thể là value trap.

## 14. DART reading order cho bank/financial group

Đọc một financial group theo sequence khác manufacturer:

```text
1. Group/subsidiary structure
2. Segment contribution
3. Interest earning assets / funding
4. NIM and loan growth
5. Asset-quality indicators
6. Provision / credit cost
7. Capital adequacy / RWA
8. Non-bank subsidiaries
9. Related-party / governance
10. Dividend and capital allocation
```

Nếu chỉ đọc income statement, bạn nhìn thấy output nhưng không nhìn thấy risk inventory nằm trong balance sheet.

## 15. Common misconceptions

### “Rate tăng thì bank chắc chắn hưởng lợi”

Sai vì asset yield, deposit cost, credit demand và credit loss phản ứng với tốc độ khác nhau.

### “Loan growth càng cao càng tốt”

Sai vì underwriting quality và risk-adjusted pricing quyết định value.

### “Bank có nhiều cash nên rất an toàn”

Cash/liquidity chỉ là một dimension. Solvency phụ thuộc asset quality, capital và loss absorption.

### “Diversified financial group ít rủi ro hơn”

Diversification có thể giảm concentration nhưng tạo thêm market, insurance, operational và governance risks.

## 16. Research exercise

Khi tự cập nhật case bằng filing mới, hãy dựng bảng 5 năm:

| Driver | Y-4 | Y-3 | Y-2 | Y-1 | Y0 |
|---|---:|---:|---:|---:|---:|
| Loans | | | | | |
| Deposits | | | | | |
| NIM | | | | | |
| Credit cost | | | | | |
| Delinquency / NPL | | | | | |
| Net income | | | | | |
| ROE | | | | | |
| CET1 | | | | | |
| RWA | | | | | |

Sau đó giải thích **mechanism** của mỗi inflection point thay vì chỉ mô tả tăng/giảm.

## Mental Model cuối

> Một Korean financial group là một machine biến funding và regulatory capital thành risk-adjusted financial assets/services. Earnings chỉ là flow của một năm; chất lượng thật nằm trong franchise funding, underwriting, asset quality, capital buffer và khả năng phân bổ capital giữa các subsidiaries.

Case tiếp theo nên đọc cùng [07_lg_energy_solution_battery_case](./07_lg_energy_solution_battery_case.md) để thấy sự khác biệt giữa **balance-sheet-intensive finance** và **CAPEX-intensive manufacturing**.