# Forensic Accounting, Earnings Quality và Red Flags khi đọc doanh nghiệp Hàn Quốc (포렌식 회계·이익의 질·회계 경고신호)

Financial statements không phải lời nói dối mặc định, nhưng cũng không phải “sự thật kinh tế” hoàn hảo. Accounting là hệ thống measurement dựa trên rules, estimates và timing assumptions. Vì vậy cùng một mức reported profit có thể có chất lượng rất khác nhau.

**Earnings quality / 이익의 질** hỏi một câu thực tế: phần lợi nhuận đang thấy có phản ánh economics lặp lại, có convert thành cash, có dựa quá nhiều vào estimate hay one-off, và có bền vững qua cycle hay không?

Forensic accounting không có nghĩa đi săn fraud ở mọi company. Mục tiêu là nhận ra nơi accounting có thể che business deterioration, làm profit trông tốt hơn cash economics, hoặc khiến analyst hiểu sai risk.

Chapter này mở rộng [`09_disclosure_accounting_dart_kind.md`](./09_disclosure_accounting_dart_kind.md) và biến việc đọc báo cáo thành một process kiểm tra consistency.

## 1. Profit không bằng cash

Accrual accounting ghi nhận revenue/cost theo economic event, không chỉ theo cash receipt/payment.

Điều đó cần thiết. Nếu chỉ dùng cash accounting, một project dài hạn sẽ rất khó phản ánh performance.

Nhưng accrual tạo khoảng cách giữa reported income và cash.

Một starting relation:

\[
CFO \approx Net\ Income + Noncash\ Charges - Working\ Capital\ Investment + Other\ Adjustments
\]

Nếu net income tăng nhiều năm nhưng CFO không đi cùng, cần tìm reason.

## 2. Earnings quality là gì?

High-quality earnings thường có vài đặc điểm:

- đến từ core business;
- cash conversion hợp lý;
- không phụ thuộc lớn vào one-off gain;
- estimate không quá aggressive;
- repeatable trong normal conditions;
- không được tạo chủ yếu bằng giảm investment cần thiết.

Low-quality earnings không nhất thiết illegal. Nó có thể hoàn toàn GAAP-compliant nhưng ít predictive value.

## 3. Accruals

**Accrual / 발생액** là chênh lệch giữa accounting earnings và cash-related realization.

Một simple lens:

\[
Total\ Accruals \approx Net\ Income - CFO
\]

Nếu accruals persistently cao, hỏi company đang recognize revenue sớm, defer costs hay working capital đang deteriorate.

Nhưng cyclical inventory build hoặc rapid growth cũng có thể làm accrual cao hợp lý. Context luôn cần thiết.

## 4. Receivables tăng nhanh hơn revenue

Nếu revenue tăng 10% nhưng accounts receivable tăng 40%, có thể là:

- customer payment terms dài hơn;
- mix chuyển sang customers trả chậm;
- company push sales bằng generous credit;
- collection quality xấu;
- revenue recognition aggressive.

Một metric:

\[
DSO = \frac{Average\ Receivables}{Revenue} \times Days
\]

DSO tăng không phải proof fraud. Nó là signal để hỏi quality của sales.

## 5. Inventory tăng nhanh

Inventory có thể tăng vì growth preparation, supply-chain buffer hoặc new product launch.

Nhưng nếu inventory tăng trong khi demand yếu, risk gồm markdown, obsolescence và cash lock-up.

Với semiconductors, electronics, fashion, chemicals hoặc autos, inventory quality phải đọc theo cycle.

Useful questions:

```text
Inventory volume tăng vì capacity hay unsold goods?
Finished goods hay raw materials tăng?
Inventory days trend?
Provision/impairment?
```

## 6. Payables tăng và cash flow “đẹp” tạm thời

Company có thể cải thiện CFO bằng kéo dài payment to suppliers.

Nếu DPO tăng mạnh, CFO có thể tốt hơn dù operational economics không đổi.

\[
CCC = DIO + DSO - DPO
\]

Cash flow improvement do supplier financing không nhất thiết repeatable.

Đây còn là signal về bargaining power hoặc liquidity stress.

## 7. Contract assets và unbilled revenue

Construction, SI, shipbuilding và long-term project businesses có thể recognize revenue trước billing/cash collection theo progress rules.

**Contract asset / 계약자산** tăng nhanh hơn revenue cần được hiểu kỹ.

Câu hỏi:

- progress measurement method?
- customer acceptance condition?
- billing milestone?
- collection history?
- cost estimate revision risk?

Project accounting cho management nhiều estimate hơn simple retail sale.

## 8. Percentage-of-completion risk

Nếu project margin được estimate sớm nhưng cost overrun xuất hiện muộn, profit ban đầu có thể bị overstated tương đối.

Ví dụ project contract = 100, expected cost = 80 → expected margin = 20.

Nếu halfway later expected cost rises to 95, cumulative recognized margin phải adjust.

Do đó backlog lớn không tự động nghĩa future profit chắc chắn.

## 9. Revenue recognition: shipment không phải lúc nào cũng economic completion

Revenue recognition phụ thuộc transfer of control/performance obligation, không đơn giản “invoice issued”.

Red-flag questions:

- return rights?
- bill-and-hold?
- channel stuffing?
- consignment?
- related-party sales?
- unusual quarter-end spike?

Không nên accuse misconduct; chỉ cần kiểm tra terms.

## 10. One-off gains

Net income có thể tăng nhờ:

- asset disposal gain;
- stake sale;
- fair-value gain;
- FX gain;
- litigation settlement;
- reversal of provision.

Nếu mục tiêu là normalized earnings, phải tách recurring operation khỏi one-off.

Một company bán building rồi report record net income không có nghĩa core profitability tăng.

## 11. Operating profit cũng có thể chứa judgment

Nhiều analyst tin operating profit “sạch” hơn net income. Thường đúng hơn, nhưng vẫn cần xem classification.

Ví dụ capitalization of development costs có thể chuyển expense hôm nay thành asset amortized sau này.

Nếu company capitalize nhiều hơn peers, current operating profit có thể cao hơn tương đối.

## 12. Capitalized development cost

R&D có thể gồm expense và capitalized development asset tùy criteria.

Economic question:

> Chi phí này thực sự tạo future economic benefit đủ chắc để asset hóa chưa?

Nếu capitalization tăng nhanh nhưng commercial success yếu, impairment có thể đến sau.

Đặc biệt relevant trong software, game, biotech và technology development.

## 13. CAPEX vs repair expense

Capitalizing cost làm current expense thấp hơn, asset cao hơn, sau đó depreciation/amortization xuất hiện nhiều kỳ.

Nếu management classify routine maintenance thành capital asset quá aggressive, short-term profit có thể được boost.

Analyst nên compare CAPEX, depreciation và asset age với peers/history.

## 14. Depreciation assumptions

Useful life dài hơn → annual depreciation thấp hơn → profit cao hơn.

Thay đổi useful life hoặc residual value có thể legitimate khi technology/asset use thay đổi, nhưng cần understand impact.

Trong capital-intensive industry, depreciation policy materially affects EBIT.

## 15. Provision và reserve

**Provision / 충당부채** ghi expected obligation khi amount/timing uncertain.

Examples:

- warranty;
- litigation;
- restructuring;
- environmental cost;
- credit loss.

Estimate thấp quá có thể làm current profit cao hơn; estimate cao trong good year rồi reverse sau có thể smooth earnings.

## 16. Warranty reserve

Auto/electronics company tăng sales nhưng warranty provision rate giảm mạnh cần explanation.

Có thể quality thật sự tốt hơn. Cũng có thể assumption optimistic.

Later recall có thể làm cost jump.

## 17. Expected credit loss

Bank/finance/receivable-heavy company phải estimate expected losses.

Nếu loan growth nhanh nhưng provision ratio giảm trong khi borrower quality không cải thiện rõ, analyst nên deep-dive.

Provision timing là core part của earnings quality trong financial institutions.

## 18. Deferred tax asset

**Deferred tax asset / 이연법인세자산** có value nếu company có future taxable profit để use deductions/losses.

Loss-making company với large DTA cần assess recoverability assumption.

Accounting recognition không biến tax loss carryforward thành cash ngay.

## 19. Related-party transactions

Related-party sales, loans, guarantees hoặc asset transfers có thể hoàn toàn legitimate trong group structure.

Nhưng chúng cần extra scrutiny vì price/terms có thể không giống arm's-length market.

Hỏi:

```text
Counterparty là ai?
Transaction size?
Pricing basis?
Payment terms?
Receivable outstanding?
Guarantee?
```

Xem [`08_corporate_governance_ownership_and_control.md`](./08_corporate_governance_ownership_and_control.md).

## 20. Consolidated vs separate statements

Profit ở parent separate statement có thể đến từ dividends từ subsidiaries, trong khi consolidated economics khác.

Ngược lại, profitable subsidiary có thể bị offset bởi loss ở entity khác trong consolidation.

Do đó luôn xác định perimeter trước khi compare ratios.

## 21. Non-controlling interest

Consolidated net income có thể gồm profit attributable to non-controlling interests.

Nếu analyst dùng total consolidated profit nhưng valuation chỉ cho parent common shareholders, cần lấy phần **attributable to owners of parent** phù hợp.

## 22. Equity-method income

Company sở hữu associate có thể recognize share of profit mà không receive equivalent cash dividend.

Equity-method earnings tăng nhưng cash upstream hạn chế có thể làm holding-company liquidity khác apparent profit.

## 23. Cash balance không phải luôn freely available

Cash có thể:

- restricted;
- pledged;
- nằm ở regulated subsidiary;
- nằm ở overseas entity;
- cần cho working capital.

Vì vậy “cash = X” không đồng nghĩa X hoàn toàn available cho dividend/debt repayment.

## 24. Net cash company vẫn có risk

Một company có net cash nhưng:

- large purchase commitments;
- guarantees;
- pension deficit;
- litigation;
- growth CAPEX commitments.

Balance-sheet headline có thể quá optimistic nếu bỏ footnotes.

## 25. Off-balance-sheet và contingent exposure

Look for:

- guarantees;
- leases;
- take-or-pay contracts;
- JV commitments;
- PF support;
- derivatives;
- supplier finance;
- factoring with recourse.

Economic leverage có thể lớn hơn accounting borrowings.

## 26. Factoring receivables

Nếu company sell receivables, CFO/liquidity có thể improve.

Nhưng cần hỏi transfer có truly remove risk không. Nếu company retains recourse, credit risk vẫn partly quay lại.

Repeated factoring để maintain cash flow có thể signal working-capital pressure.

## 27. Supplier finance

Supplier-finance arrangement có thể economically giống borrowing nhưng nằm gần trade payables.

Nếu payment term được kéo dài nhờ finance provider, analyst nên consider whether part of payable should be viewed as financial debt.

## 28. Sale-and-leaseback

Company bán asset rồi lease lại tạo immediate cash nhưng future lease payments tăng.

Không nên coi toàn bộ proceeds như value creation. Đây là financing/asset-structure change.

## 29. Frequent “non-recurring” charges

Nếu restructuring charge xuất hiện năm nào cũng có, nó không còn truly non-recurring.

Normalized earnings không nên add back mọi “one-off” management label.

Một rule:

> Nếu một loại charge lặp nhiều cycle, hãy treat ít nhất một phần như normal cost of doing business.

## 30. Adjusted EBITDA

Company IR có thể report adjusted EBITDA loại nhiều items.

Useful nếu adjustments thật sự unusual. Nhưng analyst phải reconcile về audited numbers.

Questions:

- stock compensation removed?
- restructuring every year?
- acquisition cost recurring?
- lease treatment consistent?

Adjusted metric không sai; problem là khi adjustment xóa economic cost thật.

## 31. Share-based compensation

Share-based compensation không phải immediate cash outflow nhưng là real economic cost vì dilute owners.

Ignoring it hoàn toàn có thể overstate owner economics.

## 32. Buyback che dilution

Company có thể buy back shares nhưng đồng thời issue shares/options cho employees or acquisition.

Do đó check **net share count**, không chỉ gross buyback announcement.

## 33. Tax rate bất thường

Effective tax rate có thể biến động vì deferred tax, foreign mix, tax credits hoặc one-off.

Nếu net income jump chủ yếu vì tax benefit, core operating economics chưa chắc cải thiện.

Normalize tax when forecasting.

## 34. FX gains/losses

Exporter/importer có thể có FX effect trong operating/non-operating items tùy exposure/accounting.

Temporary KRW move có thể boost earnings nhưng không nên extrapolate như structural margin gain.

Xem [`21_economy_to_company_transmission.md`](./21_economy_to_company_transmission.md).

## 35. Pension assumptions

Defined-benefit obligations phụ thuộc discount rate, salary growth và demographic assumptions.

Lower discount rate thường làm liability present value tăng.

Pension deficit có thể là quasi-debt-like claim cần xem trong long-term analysis.

## 36. Auditor opinion

Audit opinion không phải guarantee company healthy. Auditor chủ yếu opine financial statements materially conform to accounting framework.

Still, qualified/adverse/disclaimer opinion hoặc emphasis matters đáng đọc kỹ.

Change of auditor, repeated restatement hoặc material weakness signal cũng đáng attention.

## 37. Restatement

**Restatement / 재작성·정정공시** xảy ra khi prior numbers cần correction.

Một small typo khác hoàn toàn material correction affecting revenue/profit/equity.

When restatement appears, ask:

- what changed?
- periods affected?
- cash impact?
- control weakness?
- management credibility?

## 38. Quarter-end behavior

Nếu Q4 luôn có unusual revenue surge, receivable increase hoặc inventory adjustment, investigate seasonality vs accounting pressure.

Do not infer manipulation automatically. Many industries genuinely seasonal.

The key is consistency between operational explanation and cash/working-capital pattern.

## 39. Beneish-style mindset, không mechanical score

Academic forensic models combine accrual, receivables, margins và leverage to flag manipulation risk. Useful as screening, not verdict.

A score cannot understand industry-specific accounting better than detailed analysis.

Use models to ask better questions, not to accuse.

## 40. Cash conversion ratio

One lens:

\[
Cash\ Conversion = \frac{CFO}{Net\ Income}
\]

Long-run ratio around reasonable levels can support earnings quality. But high CAPEX business, financial firms or rapid-growth firms require context.

One year ratio is rarely decisive.

## 41. FCF quality

FCF can be “improved” by cutting CAPEX below maintenance need.

If old factory needs 500 annual maintenance but company spends 200 to show FCF, future reliability/capacity may deteriorate.

Thus:

```text
Reported FCF
≠ sustainable owner cash flow
```

Need distinguish maintenance vs growth CAPEX conceptually.

## 42. Earnings quality bridge

A useful bridge:

```text
Reported Net Income
- one-off gains
+ one-off losses judged truly non-recurring
± accounting normalization
= Normalized Earnings

Normalized Earnings
± working-capital normalization
- maintenance CAPEX
= Sustainable Cash Earnings approximation
```

This is not official accounting. It is analyst reconstruction.

## 43. Forensic workflow trên DART

Khi review company:

```text
1. Compare 5 years income statement
2. Compare CFO vs net income
3. Track receivable/inventory/payable days
4. Read accounting policies
5. Read major estimates/provisions
6. Read related-party notes
7. Read commitments/guarantees
8. Reconcile non-GAAP/IR metrics
9. Search corrections/restatements
10. Build normalized earnings bridge
```

## 44. Red-flag cluster quan trọng hơn single signal

Receivable increase một mình có thể harmless. Inventory increase một mình cũng có thể growth.

Nhưng cluster:

```text
Revenue growth slows
+ receivables accelerate
+ inventory accelerates
+ CFO falls
+ factoring increases
+ debt rises
```

thì risk picture mạnh hơn rất nhiều.

Forensic analysis là pattern recognition across statements.

## 45. Example: SI/SM company

Một IT-services company có revenue tăng nhờ long-term projects. Nhưng contract assets tăng nhanh, subcontractor payables tăng và cash collection chậm.

Reported operating margin stable, nhưng CFO negative hai năm.

Analysis không kết luận “fraud”. Instead:

```text
Project mix changed?
Milestone billing delayed?
Customer acceptance issue?
Cost estimate aggressive?
Subcontractor financing supporting cash?
```

This is a proper forensic question set.

## 46. Example: manufacturer

Manufacturer report profit growth 20%, nhưng inventory +50%, receivable +35%, utilization falling và discounting increasing.

Possible interpretation: production ahead of demand and channel pressure.

Need compare industry cycle, inventory category và subsequent sales.

## 47. Example: holding company

Holding company shows high accounting profit from equity-method affiliates but parent standalone cash low.

Debt maturity at parent cannot be paid automatically by subsidiary profit unless dividends/asset sales upstream cash.

This illustrates difference between economic ownership and liquidity.

## Mental Model

> Accounting quality analysis là kiểm tra xem **reported earnings → balance-sheet changes → cash flow → economic reality** có kể cùng một câu chuyện hay không.

Flow:

```text
Revenue claim
→ receivable / cash
→ margin
→ inventory / cost / provision
→ operating cash flow
→ capex / financing
→ final liquidity
```

Nếu một link trong chain diverges, đừng vội kết luận; hãy tìm explanation trong business model và footnotes.

## Common misconceptions

**“CFO thấp hơn net income = fraud.”** Sai. Growth và working capital có thể giải thích hợp lý.

**“Audited = không có risk.”** Sai. Audit giảm material misstatement risk nhưng không đảm bảo business economics tốt.

**“One-off nên add back hết.”** Sai. Chi phí lặp lại dưới nhiều tên khác nhau vẫn là economic cost.

**“Goodwill impairment không cash nên bỏ qua.”** Cash outflow đã xảy ra khi acquisition; impairment có thể là evidence capital allocation trước đó kém.

**“Net cash nghĩa balance sheet an toàn.”** Chưa chắc nếu commitments/guarantees lớn.

## Liên kết tiếp theo

- [`09_disclosure_accounting_dart_kind.md`](./09_disclosure_accounting_dart_kind.md)
- [`11_banks_finance_and_corporate_funding.md`](./11_banks_finance_and_corporate_funding.md)
- [`20_how_to_analyze_a_korean_company.md`](./20_how_to_analyze_a_korean_company.md)
- [`36_credit_ratings_bonds_default_and_restructuring.md`](./36_credit_ratings_bonds_default_and_restructuring.md)
- [`37_corporate_actions_mna_mergers_spin_offs_and_capital_actions.md`](./37_corporate_actions_mna_mergers_spin_offs_and_capital_actions.md)