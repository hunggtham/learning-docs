# 05 — Cross-Border Investing: Currency, Tax Wrappers, Market Access và thực hành Hàn–Việt

> Đầu tư quốc tế không chỉ là mua một asset tốt ở quốc gia khác. Return thực tế còn phụ thuộc currency, account wrapper, tax friction, custody, settlement, market-access rules, liquidity, capital controls và nơi bạn sẽ sử dụng tiền trong tương lai. Chapter này xây framework bền vững thay vì ghi cứng những tax rate hoặc regulation có thể thay đổi.

## 1. Bắt đầu từ Economic Exposure, không bắt đầu từ nơi niêm yết

Một ETF niêm yết ở Korea có thể sở hữu US equities, Japanese bonds hoặc gold. Listing venue chỉ nói nơi bạn trade wrapper; **economic exposure** nằm ở underlying cash flows.

Vì vậy country allocation nên phân loại theo underlying economy/currency/factor, không chỉ exchange ticker.

## 2. Ba Currency cần phân biệt

Cross-border investor nên tách:

```text
Trading Currency
Underlying Economic Currency
Liability Currency
```

Trading currency là đồng tiền dùng settlement. Underlying currency là currency của cash flows/assets. Liability currency là currency bạn cần cho future spending.

Một Korean-listed US ETF giao dịch KRW nhưng vẫn có USD economic exposure nếu unhedged.

## 3. Reporting Currency

Account có thể hiển thị mọi asset quy đổi về KRW. Đây chỉ là **reporting currency**. Việc app hiển thị KRW không xóa USD/VND risk.

Risk dashboard nên giữ cả local return và home-currency return.

## 4. FX Return Decomposition

Exact relationship gần:

```text
Home Return = (1 + Local Asset Return) × (1 + FX Return) - 1
```

Approximation cho moves nhỏ:

```text
Home Return ≈ Asset Return + FX Return
```

Interaction term trở nên material khi moves lớn.

## 5. Example: USD Asset từ góc nhìn KRW

Nếu US stock +10% USD và USD/KRW +8% (USD mạnh so KRW), KRW return lớn hơn 18% do interaction. Nếu USD/KRW -8%, phần lớn equity gain có thể bị offset.

Điều này giải thích vì sao headline S&P return không bằng return investor ở Korea nhận.

## 6. Natural Hedge

Nếu future liability bằng USD, owning USD assets có thể tạo natural hedge. Nếu liability là mua nhà ở Korea, KRW liability lớn khiến excessive USD/VND exposure tạo mismatch.

Hedging decision nên bắt đầu từ balance sheet cá nhân, không từ FX forecast ngắn hạn.

## 7. Human Capital cũng có Currency Exposure

Salary và career income là một asset-like stream. Người nhận lương KRW đã có substantial KRW human-capital exposure.

Điều này có thể justify some foreign assets for diversification, nhưng future Korean housing/liabilities vẫn kéo ngược lại. Household balance sheet nên nhìn tổng thể.

## 8. Currency Diversification khác Currency Speculation

Owning foreign currencies để diversify purchasing power khác việc timing USD/KRW hàng tuần.

Strategic currency allocation dựa liabilities và portfolio role; tactical FX bet dựa forecast. Không nên trộn hai mục tiêu.

## 9. Hedged vs Unhedged Return

Currency-hedged fund dùng forwards/swaps để giảm FX movement. Hedging có cost/benefit từ rate differential, basis, transaction cost và imperfect hedge.

Unhedged exposure có thể diversify risk-off regimes nếu foreign currency acts safe haven, nhưng relationship không guaranteed.

## 10. Forward Points

FX forward price phản ánh interest-rate differential theo no-arbitrage intuition. Currency có higher rate thường trade at forward discount relative to lower-rate currency under conventional quote framework.

Hedge cost không nên được mô tả đơn giản là “fee”; carry economics là phần lớn effect.

## 11. Hedge Ratio

Hedge không nhất thiết 0% hoặc 100%. Investor có thể hedge partial exposure.

Một liability-driven approach định nghĩa target net currency exposure rồi chọn hedge ratio đủ đưa portfolio gần target.

## 12. Dynamic vs Static FX Hedge

Static hedge giữ fixed ratio; dynamic hedge thay theo valuation/volatility/liability. Dynamic adds model/turnover risk.

Nếu không có robust process, simple strategic ratio thường dễ quản lý hơn macro timing.

## 13. Wrapper Risk

ETF/ETN/fund wrapper thêm layer ngoài underlying. Cần hiểu legal structure, replication, collateral, counterparty, tracking và liquidation rules.

Two products same index can have different realized return and operational risk.

## 14. Korean-listed Foreign ETF

Ưu điểm có thể gồm local account convenience, KRW settlement và compatibility với account wrappers. Nhưng evaluate benchmark, physical/synthetic replication, hedged status, tracking difference, AUM, spread, distribution treatment và underlying market hours.

Local listing không biến foreign risk thành domestic risk.

## 15. Direct Foreign Securities

Direct ownership có thể cho deeper liquidity, broader product choice và lower fund tracking layer. Đổi lại FX conversion, tax/reporting, market hours, estate/legal và account complexity có thể tăng.

Decision nên dựa total implementation cost và operational capacity.

## 16. ETF Premium / Discount

ETF market price có thể lệch NAV/iNAV, đặc biệt khi underlying market đóng, stressed hoặc illiquid.

Local ETF tracking US market trong Asian hours phải price US futures/FX/news, nên apparent premium có thể phản ánh stale NAV hơn true arbitrage.

## 17. Holiday Mismatch

Korea, Vietnam, US và Europe có holidays khác. Wrapper có thể trade khi underlying closed hoặc ngược lại.

Spreads thường wider khi price discovery yếu. Avoid treating normal NAV relationships as guaranteed on mismatched holidays.

## 18. Time-Zone Risk

Information may arrive when your local market closed. Gap risk matters for direct foreign positions and local wrappers.

If you cannot monitor overnight, position sizing should reflect inability to react, not rely on stop orders as perfect protection.

## 19. Settlement Cycle

Trade execution and settlement are different. Buying power may update before withdrawable cash.

Cross-border cash management must consider settlement, FX conversion, bank transfer and holiday calendars together.

## 20. Prefunding

Some markets/accounts require cash/securities available before order. Others allow different settlement flexibility.

Operational rules can change; verify broker/exchange current requirements before real trade.

## 21. Custody Chain

Ask who is legal broker, custodian/sub-custodian and depository. Client asset segregation matters if broker fails.

Brand reputation alone does not tell custody structure.

## 22. Brokerage Legal Entity

A global brand may operate through different regulated entities by jurisdiction. Investor protection and complaint process can differ.

Always confirm contract counterparty entity, especially for OTC/CFD products.

## 23. Securities Lending

Some brokers/funds lend securities. Lending can create income but introduces borrower/collateral/operational considerations.

Know whether participation is optional and how proceeds/risks are handled.

## 24. Market Access Korea

Korea offers domestic equities, ETFs, ETNs, bonds and derivatives plus access to foreign securities through brokers. Product availability and tax/account rules change.

Framework: underlying → wrapper → account → execution → after-tax outcome.

## 25. Market Access Vietnam

Vietnam has local market structure, foreign ownership constraints and custody/account rules. For foreign investor, access and repatriation are separate risk layers from stock fundamentals.

Always verify current official/broker rules before implementation.

## 26. Foreign Ownership Limit

Some Vietnamese sectors/companies can have foreign ownership constraints. Near-full room may affect accessibility and valuation/technical flow.

Do not confuse access premium with business intrinsic value.

## 27. Free Float

Headline market cap overstates investable liquidity if controlling shareholders hold large stake. **Free-float market cap** matters for index weight and execution.

Cross-border investor should compare position size with free-float turnover, not total market cap.

## 28. Daily Price Limits

Vietnam price bands can make stop-loss non-executable in panic. Several floor sessions with no buyers can create realized loss far beyond planned trigger.

Liquidity-adjusted position sizing is essential.

## 29. Repatriation Risk

After selling, can proceeds be transferred home easily? What documentation, tax clearance or banking process is required?

This is operational/country risk invisible in P/E.

## 30. Capital Controls

Capital-account rules can tighten during stress. Even if normal-times process is easy, tail scenario deserves consideration for emerging-market exposure.

Framework should include ability to move capital, not just asset price.

## 31. Tax Wrapper

ISA, retirement/pension accounts or other tax-advantaged wrappers can materially change net return. Eligibility, contribution limits, withdrawal and allowed products evolve.

Compare on after-tax basis and verify current official rules.

## 32. Tax Location

Some assets generate high distributions, others mostly deferred capital gain. Account location can affect tax drag.

Optimal tax location is jurisdiction-specific; chapter focuses decision logic, not fixed rates.

## 33. Withholding Tax

Foreign dividends/interest may face source-country withholding before home-country tax. Treaty/account wrapper can affect treatment.

Headline yield is not net cash yield.

## 34. Capital Gains Treatment

Taxation can differ by security type, account and residence. Cross-border investor should distinguish realized/unrealized gains and local/foreign classification.

Do not optimize based on outdated rate remembered from previous year.

## 35. Tax Residency

Tax obligations depend on residency and sometimes domicile/citizenship. Moving countries can change reporting and wrapper suitability.

Large/complex cases require professional tax/legal verification.

## 36. Estate / Inheritance Risk

Direct foreign ownership may create estate/inheritance considerations. Wrapper vs direct security can differ legally.

This becomes important as asset size grows and should be part of operational planning.

## 37. Documentation Discipline

Store trade confirmations, FX conversion records, dividend/withholding statements, account statements and tax documents.

Multi-year reconstruction is difficult; documentation is part of investment process.

## 38. Cost Stack

Total cost can be expressed conceptually:

```text
Broker Commission
+ Exchange / Regulatory Fees
+ Bid-Ask Spread
+ Slippage
+ FX Spread
+ Fund Expense / Tracking Difference
+ Funding / Borrow Cost
+ Tax / Withholding
```

Lowest advertised commission may not be cheapest implementation.

## 39. FX Conversion Cost

Frequent small conversions can compound spread/fees. Consider conversion policy, minimum fee and whether broker auto-converts dividends.

Currency management should minimize unnecessary churn.

## 40. Dividend Currency

Dividend may arrive in underlying currency or auto-convert. Auto conversion changes net currency exposure and costs.

Know account policy before relying on dividend as cash-flow hedge.

## 41. Liquidity Comparison Korea vs Vietnam

Korean large caps and major ETFs are generally deeper than many Vietnam small/mid caps, but product-specific liquidity always matters.

Position size should be defined relative to realistic exit capacity under stressed volume.

## 42. Market Impact

A cross-border investor using less-liquid securities must estimate how many days to exit without dominating volume.

Market order urgency can convert paper return into slippage loss.

## 43. Korea Sector Concentration

Broad Korea exposure often embeds semiconductor/exporter/industrial/financial sensitivity. Adding separate semiconductor ETF may duplicate same macro factor.

Diversification by ticker is not factor diversification.

## 44. Vietnam Sector Concentration

Vietnam index exposure can be heavy in banks/property/consumer. Broad index still carries domestic credit/property cycle.

Understand index methodology and weights before assuming “country ETF = diversified”.

## 45. Common Macro Factors

Korea and Vietnam differ structurally but share exposure to USD, China, global trade and risk sentiment.

Cross-country diversification may weaken exactly during global deleveraging.

## 46. Fed Shock

Hawkish Fed can raise US yields/USD. Korea transmits quickly through KRW, exporters/foreign flows and valuation. Vietnam can transmit through USD/VND pressure, domestic liquidity/policy room and sentiment.

Speed and policy response differ.

## 47. China Shock

Korea has direct export/industrial sensitivity. Vietnam has trade, tourism, input and FDI-relocation channels.

A China slowdown can hurt demand yet lower commodity/input costs or accelerate supply-chain relocation.

## 48. Oil Shock

Korea as energy importer can face terms-of-trade and inflation pressure. Vietnam has mixed importer/producer/regulated-price channels.

Company effect depends sector spread economics, not country headline alone.

## 49. Country Risk Premium

Political/regulatory/institutional uncertainty can raise discount rate even when company cash flows look good.

Country risk should affect required return and position size, not only narrative.

## 50. Currency Buckets

Aggregate portfolio by KRW, USD, VND and other economic exposures. Compare with future liabilities by currency.

This reveals hidden mismatch that account-by-account view misses.

## 51. Country Buckets

Classify underlying country risk separately from listing venue. Korean-listed US ETF belongs economically largely to US/Global bucket plus Korean wrapper characteristics.

## 52. Factor Buckets

Cross-border positions should also be grouped by equity beta, duration, credit, commodities, growth, value and liquidity.

Multiple countries can still share same factor.

## 53. Home Bias

Familiarity can make domestic assets feel safer than they are. Salary, property and career may already concentrate domestic risk.

But foreign diversification also adds FX/tax/operational complexity. Goal is balanced total risk, not maximum foreign allocation.

## 54. Liability-Driven Allocation

Near-term liabilities should be matched by currency and liquidity. Money needed for Korea housing soon should not depend on VND equity liquidity or USD stock recovery.

Long horizon allows more mismatch but still requires explicit policy.

## 55. Emergency Liquidity

Cross-border transfers can be delayed by holidays, settlement or documentation. Keep emergency cash in accessible liability currency rather than treating foreign portfolio as instant liquidity.

## 56. Cross-Border IPS

A useful Investment Policy Statement should define target country/currency allocation, maximum FX mismatch, permitted wrappers, liquidity floor, documentation process, rebalancing bands and verification rules for tax/regulation changes.

## 57. Product Comparison Template

When comparing Korean local ETF vs direct US ETF vs another wrapper, compare:

```text
Underlying Exposure
Currency Hedge
Expense / Tracking
Spread / Liquidity
Tax Wrapper Eligibility
Dividend Treatment
FX Conversion
Settlement / Market Hours
Estate / Legal Complexity
Operational Simplicity
```

Expected return should be compared after expected frictions.

## 58. Rebalancing Across Currencies

Rebalancing can use new contributions to reduce FX conversions/tax realization. Sell/buy only when net benefit exceeds friction.

Currency rebalancing and asset-class rebalancing are separate dimensions.

## 59. Stress Testing

Stress scenarios should combine asset + FX + liquidity. Example: Korean equity -20%, VND equity -30%, KRW weak 10%, VND weak 5%, spreads widen and foreign-market access slower.

Single-factor stress underestimates real cross-border tails.

## 60. Operational Failure Scenario

Ask what happens if broker unavailable, bank transfer delayed, account temporarily restricted or documents missing. Keep backup liquidity and records.

Operational resilience is part of portfolio risk management.

## 61. Snapshot Discipline

Tax, settlement, account rules and foreign-room framework change over time. Permanent notes should explain concepts; real-money decision should verify current regulator/exchange/broker/tax-authority source.

This prevents knowledge library becoming stale policy manual.

## 62. Pre-Trade Workflow

```text
1. Identify underlying economic exposure.
2. Identify all currencies.
3. Check wrapper/legal claim.
4. Check liquidity/free float.
5. Check settlement/market hours.
6. Check account/tax wrapper eligibility.
7. Estimate total cost.
8. Check tax/withholding/repatriation.
9. Stress asset + FX + liquidity.
10. Size relative to liabilities and total portfolio.
```

## 63. Post-Trade Review

Separate local asset return, FX return, income, tax, fees and implementation. This shows whether cross-border exposure added security alpha, currency beta or simply extra friction.

## 64. Mental Model cuối cùng

Cross-border investing is a multi-layer balance-sheet problem:

```text
Underlying Business / Asset
+ Country Risk
+ Currency Risk
+ Wrapper / Counterparty
+ Custody / Settlement
+ Liquidity
+ Tax / Withholding
+ Repatriation
+ Liability Currency
= Real Investor Outcome
```

Khi từng layer được tách rõ, lựa chọn giữa Korean ETF, direct foreign security và Vietnamese asset trở thành một quyết định có cấu trúc thay vì chỉ so chart return.