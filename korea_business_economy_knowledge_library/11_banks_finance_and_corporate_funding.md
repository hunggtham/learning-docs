# Ngân hàng, tài chính và cách doanh nghiệp huy động vốn (Corporate Funding / 기업금융과 자금조달)

Một doanh nghiệp có thể profitable trên paper nhưng vẫn phá sản nếu cash đến sai thời điểm. Vì vậy corporate finance không chỉ hỏi “business có lời không?” mà còn hỏi **business được tài trợ bằng nguồn vốn nào, kỳ hạn ra sao, lãi suất thế nào, currency nào và cash có về kịp trước khi nghĩa vụ đáo hạn hay không**.

Đây là distinction giữa **solvency (지급능력)** và **liquidity (유동성)**. Solvency hỏi tổng giá trị tài sản/business có đủ lớn để cover liabilities trong dài hạn không. Liquidity hỏi hôm nay company có đủ cash để trả payroll, supplier, interest và debt maturity không.

Một company có thể solvent nhưng illiquid. Đây là lý do funding structure quan trọng ngang profitability.

## Ba nguồn vốn cơ bản

Nguồn vốn doanh nghiệp có thể nén thành ba nhóm: **equity (자기자본)**, **debt (부채)** và **retained earnings / operating cash flow (유보이익·영업현금흐름)**.

Equity không có mandatory principal repayment nhưng làm dilute ownership. Debt giữ ownership nhưng tạo fixed claim: interest và principal phải trả bất kể business cycle. Retained earnings tránh issuance cost nhưng có opportunity cost vì cash đó lẽ ra có thể trả dividend hoặc buyback.

Một capital structure hợp lý không phải debt thấp nhất. Nó là structure phù hợp với volatility, asset life, cash-flow visibility và growth option của business.

## Match funding với asset life

Một nguyên tắc quan trọng là **maturity matching / 만기 대응**.

Nếu company xây factory có useful life 20 năm nhưng finance bằng short-term loan 6 tháng, project có thể economically tốt nhưng company phải refinance liên tục. Nếu credit market đóng đúng lúc, liquidity crisis xuất hiện.

Ngược lại, finance working capital 30 ngày bằng bond 10 năm có thể quá đắt và không cần thiết.

Mental model:

```text
Short-lived asset → short funding có thể phù hợp
Long-lived asset  → long funding thường an toàn hơn
```

Mismatch giữa asset duration và liability maturity là một trong các cơ chế quan trọng từng làm corporate/financial crises nặng hơn.

## Bank loan và relationship banking

Bank lending vẫn rất quan trọng trong Hàn Quốc, đặc biệt với SMEs và private companies chưa access bond/equity market sâu.

Bank đánh giá borrower qua cash flow, collateral, credit history, guarantees, sector outlook và management quality. Nhưng với SME, information asymmetry lớn hơn, nên collateral và relationship banking có weight cao.

Một khoản vay floating-rate thường có dạng:

\[
Loan\ Rate = Reference\ Rate + Credit\ Spread
\]

Reference rate phản ánh market/monetary conditions; spread phản ánh borrower risk và bank pricing.

Nếu company debt 1 nghìn tỷ KRW và effective rate tăng 1 percentage point, annual interest burden tăng xấp xỉ 10 tỷ KRW trước hedging và repayment effects.

## Fixed-rate vs floating-rate: cùng debt amount nhưng sensitivity khác nhau

Hai firms đều có 1 nghìn tỷ KRW debt nhưng risk có thể khác xa.

Firm A có 80% fixed-rate bond 5 năm. Firm B có 80% floating-rate bank loan repricing mỗi 3 tháng. Khi policy rate tăng, B chịu pressure gần như ngay; A chỉ chịu nhiều hơn khi issue/refinance debt mới.

Vì vậy monetary-policy transmission vào corporate earnings phụ thuộc **repricing schedule**, không chỉ total debt.

Xem [`01_macro_economy_and_business_cycle.md`](./01_macro_economy_and_business_cycle.md).

## Corporate bond và credit spread

Large companies có thể phát hành **corporate bonds / 회사채**. Yield investor yêu cầu thường có thể nghĩ như:

\[
Corporate\ Yield \approx Risk\ Free\ Benchmark + Credit\ Spread + Liquidity/Term\ Premium
\]

Credit spread tăng khi investor lo default hoặc liquidity. Vì vậy company funding cost có thể tăng dù central-bank rate không đổi.

**Credit rating (신용등급)** ảnh hưởng investor universe và coupon, nhưng rating không phải truth tuyệt đối. Nó là assessment có lag và methodology riêng.

Downgrade có thể tạo feedback loop:

```text
Weak cash flow
   ↓
Rating pressure
   ↓
Higher funding cost
   ↓
Lower profit / harder refinancing
   ↓
More rating pressure
```

## Maturity wall và refinancing risk

Một company có net debt moderate nhưng 70% debt đáo hạn trong 12 tháng vẫn riskier hơn firm debt lớn hơn nhưng maturity spread đều trong 7 năm.

Do đó phải đọc **maturity ladder / 만기구조**.

Refinancing risk tăng khi:

- market liquidity giảm;
- rating bị downgrade;
- collateral value giảm;
- business cycle xấu;
- FX market stress;
- investor risk appetite giảm.

Liquidity analysis luôn cần calendar, không chỉ balance-sheet snapshot.

## Working capital: profit không đồng nghĩa cash

Operating cycle thường là:

```text
Mua inventory
   ↓
Sản xuất / bán hàng
   ↓
Ghi receivable
   ↓
Thu cash
```

Trong khi supplier và payroll có thể phải trả sớm hơn.

**Cash Conversion Cycle (CCC)**:

\[
CCC = DIO + DSO - DPO
\]

`DIO` là inventory days, `DSO` là receivable days, `DPO` là payable days.

CCC dài hơn nghĩa cash bị khóa lâu hơn. Growth nhanh có thể làm funding need tăng vì inventory/receivable phình trước cash collection.

Đây là reason một fast-growing supplier có thể cần vay nhiều hơn dù profit tăng.

## Working capital và bargaining power

Payment term không chỉ là accounting detail; nó phản ánh bargaining power.

Large buyer kéo DPO từ 45 lên 90 ngày có thể cải thiện cash flow của mình. Nhưng supplier phía kia thấy DSO tăng và phải vay thêm.

Nói cách khác, strong buyer có thể “finance” một phần operation bằng balance sheet của supplier.

Đây là connection trực tiếp với [`06_sme_mid_sized_and_subcontracting_ecosystem.md`](./06_sme_mid_sized_and_subcontracting_ecosystem.md).

## Receivables financing, guarantees và policy finance

SME có thể dùng trade receivables làm funding base, hoặc nhận credit guarantees/policy finance để giảm collateral constraint.

Guarantee không xóa risk; nó chuyển risk sang guarantor nếu borrower default. Vì vậy policy guarantee nên được xem là **risk-sharing mechanism**, không phải free capital.

Policy banks và guarantee institutions có rationale khi private lender underfund project do information asymmetry, strategic externality hoặc long duration. Nhưng nếu selection yếu, capital có thể bị giữ trong low-productivity firms.

## Leverage: return amplifier và loss amplifier

Financial leverage giúp equity return tăng nếu asset return vượt cost of debt.

Ví dụ đơn giản:

```text
Asset return = 10%
Debt cost    = 4%
```

Debt có thể nâng ROE vì shareholder bỏ ít equity hơn.

Nhưng downturn đảo logic. Interest vẫn phải trả khi revenue giảm. Vì vậy leverage có **convex downside**.

Một vài metrics:

\[
Net\ Debt = Debt - Cash
\]

\[
Interest\ Coverage = \frac{EBIT}{Interest\ Expense}
\]

\[
Net\ Debt/EBITDA
\]

Không metric nào đủ một mình. EBITDA không phải cash; cash có thể restricted; EBIT có thể cyclical.

## Covenant: debt contract có thể giới hạn management

Loan/bond có thể chứa **covenants / 재무약정** như maximum leverage, minimum coverage hoặc restrictions on asset sale/dividend.

Covenant breach không nhất thiết nghĩa company bankrupt, nhưng có thể trigger renegotiation, higher spread hoặc acceleration rights.

Vì vậy analyst cần đọc notes về covenant chứ không chỉ headline debt amount.

## FX debt và currency mismatch

Company vay USD nhưng kiếm revenue KRW có **currency mismatch**. Khi KRW depreciates, debt quy đổi sang KRW tăng và interest burden có thể tăng.

Ngược lại, exporter có USD revenue có thể natural hedge USD debt.

Một mental model:

```text
Debt currency nên gần cash-flow currency
```

Nếu không, firm cần derivatives hoặc đủ pricing power để absorb FX movement.

FX mismatch là một mechanism quan trọng trong historical financial crises và vẫn relevant với global funding ngày nay.

## Hedging không xóa risk miễn phí

Forward, swap và option có thể giảm rate/FX volatility nhưng hedge có cost.

Company có thể hedge 70% USD exposure, còn 30% để open. Analyst cần biết hedge ratio, maturity và accounting treatment.

Derivative asset trên balance sheet không đồng nghĩa profit “chất lượng cao”; nó có thể chỉ offset loss ở underlying exposure.

## Equity issuance và dilution

Equity funding không tạo fixed repayment nhưng existing shareholders bị dilution.

Nếu company issue new shares ở price thấp hơn intrinsic value để cứu liquidity, company sống nhưng old shareholders chịu transfer.

Ngược lại, issuing equity ở high valuation để fund high-return project có thể tạo value.

Do đó “debt xấu, equity tốt” là simplification. Câu hỏi là **cost of capital và expected return của use of funds**.

## Cost of capital và hurdle rate

Project chỉ tạo value nếu expected return đủ cao so với risk-adjusted cost of funding.

Một khái niệm trung tâm là **WACC (Weighted Average Cost of Capital / 가중평균자본비용)**:

\[
WACC = w_e r_e + w_d r_d(1-T)
\]

Trong đó `w_e`, `w_d` là weights của equity/debt; `r_e`, `r_d` là cost; `T` là tax rate.

Management dùng hurdle rate để quyết định capex/M&A/R&D. Nếu funding cost tăng nhưng expected project return không đổi, NPV giảm.

## Project Finance (PF)

**Project Finance / 프로젝트 파이낸싱** tách project vào SPV và dựa nhiều vào future project cash flow hơn sponsor balance sheet.

PF phù hợp với infrastructure/real estate project có cash-flow structure riêng, nhưng contract complexity cao. Lender phải nhìn completion risk, demand risk, collateral, guarantees và waterfall.

Korean real-estate PF có thêm bridge financing, presale và contractor credit support. Xem [`18_construction_real_estate_and_project_finance.md`](./18_construction_real_estate_and_project_finance.md).

## Securities firms và non-bank finance

Hệ thống funding không chỉ có banks. Securities firms có thể underwrite bonds, securitize assets, provide bridge finance hoặc structure products. Insurers và asset managers là institutional investors mua bonds/equity.

Non-bank funding giúp diversify sources nhưng cũng có liquidity risk khác. Market-based funding thường nhạy với investor sentiment hơn relationship bank lending.

Khi market đóng, securities-based borrower có thể mất refinancing channel rất nhanh.

## Securitization: biến cash flow thành security

Receivables, mortgage hoặc loan pools có thể được securitize. Idea là tách cash flows khỏi originator và bán claims cho investors.

Securitization giúp funding và risk transfer nhưng complexity làm risk khó nhìn. Quality của underlying assets và structure waterfall quan trọng hơn label rating.

## Captive finance và industrial groups

Automotive groups thường dùng finance affiliates để support vehicle sales, lease và dealer inventory. Captive finance giúp demand nhưng làm group exposure sang credit cycle tăng.

Khi auto sales mạnh, finance affiliate hỗ trợ volume. Khi used-car prices hoặc borrower quality xấu, credit loss có thể tăng ngay cả nếu manufacturing margin chưa giảm.

Do đó group analysis cần nhìn industrial và financial affiliates cùng nhau.

## Cash không phải lúc nào cũng fungible

Một group có 20 nghìn tỷ KRW cash không có nghĩa parent có thể dùng toàn bộ.

Cash có thể nằm ở foreign subsidiaries, regulated financial affiliates hoặc JV. Dividend transfer có tax/regulatory restriction.

Vì vậy analyst phải hỏi **cash nằm ở entity nào**.

Đây là connection với [`05_group_structure_affiliates_holding_companies.md`](./05_group_structure_affiliates_holding_companies.md).

## Capital allocation: huy động vốn chỉ là nửa đầu câu chuyện

Sau khi có capital, management phải allocate giữa:

```text
Maintenance capex
Growth capex
R&D
M&A
Debt repayment
Dividend
Buyback
Cash reserve
```

Value creation phụ thuộc return của allocation chứ không phụ thuộc company “có nhiều cash”.

Một company có balance sheet mạnh nhưng repeatedly acquire low-return assets vẫn destroy value.

## Stress test funding

Một cách đọc practical là dựng scenario:

```text
Revenue -15%
EBIT margin giảm 3pt
Interest rate +150bp
KRW yếu 10%
Receivable days +20
Bond market khó refinance
```

Sau đó hỏi cash còn dương không, covenant có breach không và maturity nào trở thành critical.

Stress test hữu ích hơn một ratio duy nhất vì funding risk thường xuất hiện khi nhiều shocks xảy ra cùng lúc.

## Mental Model

> Profitability trả lời **business có tạo value không**. Funding trả lời **business có sống đủ lâu để thu được value đó không**. Capital allocation trả lời **value tạo ra được tái đầu tư có hiệu quả không**.

Một chain dễ nhớ:

```text
Operation
   ↓
Working capital
   ↓
Cash flow
   ↓
Debt / Equity funding
   ↓
Maturity + Rate + Currency risk
   ↓
Capital allocation
   ↓
Long-term value
```

## Common misconceptions

**“Debt thấp luôn tốt.”** Sai. Stable business có thể dùng moderate debt hiệu quả.

**“Cash lớn luôn an toàn.”** Sai. Cash có thể restricted hoặc nằm sai entity.

**“Profit cao nghĩa liquidity tốt.”** Sai. Receivable/inventory có thể hút toàn bộ cash.

**“Fixed-rate debt không có rate risk.”** Chỉ tạm thời. Refinancing vẫn chịu future rates.

**“Credit rating cao nghĩa không default.”** Sai. Rating là assessment xác suất, không phải guarantee.

**“Policy guarantee loại bỏ loss.”** Sai. Loss chỉ được chuyển sang party khác.

## Connections

Đọc cùng [`01_macro_economy_and_business_cycle.md`](./01_macro_economy_and_business_cycle.md), [`05_group_structure_affiliates_holding_companies.md`](./05_group_structure_affiliates_holding_companies.md), [`06_sme_mid_sized_and_subcontracting_ecosystem.md`](./06_sme_mid_sized_and_subcontracting_ecosystem.md), [`10_capital_markets_kospi_kosdaq_konex.md`](./10_capital_markets_kospi_kosdaq_konex.md), [`18_construction_real_estate_and_project_finance.md`](./18_construction_real_estate_and_project_finance.md) và [`21_economy_to_company_transmission.md`](./21_economy_to_company_transmission.md).
