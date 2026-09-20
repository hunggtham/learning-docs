# 05 — Cross-Border Investing: Currency, Tax Wrappers, Market Access và thực hành Hàn–Việt

> Đầu tư quốc tế không chỉ là mua asset tốt ở quốc gia khác. Return thực tế còn phụ thuộc currency, wrapper, custody, settlement, tax friction, foreign ownership, capital controls, liquidity và nơi bạn sẽ sử dụng tiền trong tương lai. Chapter này xây framework bền vững thay vì ghi cứng tax rates hoặc regulations dễ lỗi thời.

## 1. Bắt đầu từ Economic Exposure

Listing venue không quyết định economic exposure. Korean-listed ETF có thể sở hữu US equities; Vietnam-listed company có USD revenues; US ETF có emerging-market currency exposure.

Country allocation phải phân loại theo underlying cash flows, currency và factor exposure, không chỉ ticker/exchange.

## 2. Bốn Currency cần phân biệt

```text
Trading Currency
Underlying Economic Currency
Reporting Currency
Liability Currency
```

Trading currency dùng settlement. Underlying currency gắn với economic cash flows. Reporting currency là đơn vị app/account hiển thị. Liability currency là đồng tiền bạn cần cho future spending.

Nhầm các lớp này tạo sai assessment FX risk.

## 3. Home-Currency Return

```text
Home Return = (1 + Local Asset Return) × (1 + FX Return) - 1
```

Với moves nhỏ có thể approximate bằng asset return + FX return, nhưng interaction term material khi volatility lớn.

Korean investor nhìn S&P 500 bằng KRW phải tách equity return và USD/KRW return.

## 4. FX P/L Attribution

Post-trade review nên tách:

```text
Local Asset Return
+ Currency Translation
+ Income
+ Hedge Carry
+ Hedge Basis
- Fees / Tax / FX Conversion
```

Nếu portfolio outperform chỉ vì USD mạnh, đó không phải security-selection alpha.

## 5. Natural Hedge

Assets và liabilities cùng currency tạo natural hedge.

Nếu goal là housing deposit ở Korea trong 2 năm, KRW liability nên được funded chủ yếu bằng KRW liquid assets. Nếu future education/payment bằng USD, USD asset bucket có thể hedge tự nhiên.

## 6. Human Capital Currency

Salary/career income là implicit asset stream. Người sống/làm việc Korea có substantial KRW human-capital exposure.

Foreign assets có thể diversify domestic earning risk, nhưng housing/pension/debt liabilities vẫn cần được map separately.

## 7. Currency Diversification vs FX Speculation

Strategic FX exposure dựa liabilities và total balance sheet. Tactical FX trade dựa forecast.

Không nên dùng long-term diversification position rồi quản lý như weekly FX trade chỉ vì USD/KRW biến động.

## 8. Hedged vs Unhedged

Hedged product dùng forwards/swaps/futures để offset currency. It reduces translation volatility but creates carry/basis/tracking costs.

Unhedged exposure can be beneficial when foreign currency diversifies home-country shock. “Hedged safer” is not universally true.

## 9. Forward Points

FX forward reflects interest-rate differential under covered-interest-parity intuition plus basis/frictions.

Hedge cost is not simply management fee. Rate differential can dominate annual hedged-vs-unhedged result.

## 10. Cross-Currency Basis

Institutional funding constraints can cause cross-currency basis away from textbook parity.

Large hedged portfolios may face basis costs that change under dollar funding stress.

## 11. Strategic Hedge Ratio

Hedge ratio should reflect liability certainty, horizon and acceptable FX volatility.

Known near-term liability usually supports high hedge; long-horizon growth bucket may allow more unhedged exposure.

## 12. Dynamic Hedge

Dynamic hedge changes ratio by valuation/volatility/macro. It adds turnover and model/timing risk.

Without robust process, strategic hedge + bands is usually easier to govern.

## 13. Currency Overlay

Large portfolio may separate security selection from currency management: underlying managers hold assets while overlay manages FX forwards.

Conceptually useful even for retail: decide desired asset exposure and currency exposure separately.

# Phần II — Wrapper và Ownership

## 14. Wrapper Risk

ETF, ETN, mutual fund, direct stock and derivative can reference same market but create different legal claims.

Wrapper affects custody, tracking, issuer/counterparty, taxation, liquidity and account eligibility.

## 15. Korean-Listed Foreign ETF

Convenient KRW trading does not remove foreign underlying risk.

Check benchmark, replication, hedge status, expense, tracking difference, securities lending, distributions, AUM, spread and market-hour mismatch.

## 16. Direct Foreign Securities

Direct ownership may provide deeper liquidity/product choice and remove local-fund tracking layer.

Trade-off: FX conversion, foreign-market hours, tax/reporting, estate/legal and operational complexity.

## 17. ETF vs ETN

ETF usually fund/share claim over assets; ETN is issuer debt linked to index.

ETN adds issuer credit even when reference exposure identical.

## 18. Synthetic ETF

Swap-based replication can improve access/tracking but adds counterparty/collateral structure.

Synthetic is not automatically worse; read collateral, reset frequency and counterparty limits.

## 19. Depositary Receipt

ADR/GDR-like receipts represent foreign shares through depositary structure. Price can reflect FX, fees and local-market access constraints.

Receipt is another wrapper layer; map underlying/share ratio and conversion mechanics.

## 20. Fund Domicile

Two ETFs tracking same index but domiciled in different jurisdictions can have different tax, withholding, estate, distribution and regulatory treatment.

Domicile is separate from listing exchange and underlying country.

# Phần III — Market Hours, Price Discovery và Settlement

## 21. Time-Zone Mismatch

Korean ETF tracking US equities trades while US cash market closed. Price may use futures, FX and new information while official NAV references stale close.

Apparent premium/discount can therefore be misleading.

## 22. Holiday Mismatch

Local wrapper may trade while underlying market closed or vice versa. Spreads can widen because arbitrage/price discovery weaker.

Avoid large execution when underlying price cannot update unless strategy explicitly accounts for it.

## 23. Settlement Cycle

Trade date, security settlement, FX settlement and bank transfer can differ.

Buying power displayed by broker is not always withdrawable cash. Cross-border liquidity planning must map each step.

## 24. Prefunding

Some markets/accounts require cash/securities before order. Others allow settlement flexibility.

Rules change; verify current broker/exchange source before real transaction.

## 25. Failed Settlement

Operational error, holiday mismatch or insufficient securities/cash can create failed settlement and fees/restrictions.

Institutions manage settlement risk as separate operational process; retail should at least avoid assuming cross-border transfers are instant.

## 26. Corporate Actions across Borders

Dividends, rights offerings, tender offers, splits and votes may have earlier broker deadlines than local-market official date.

Foreign holders can face documentation/processing constraints. Read broker notice, not only company announcement.

# Phần IV — Custody và Legal Structure

## 27. Custody Chain

Map broker → custodian → sub-custodian → central depository where applicable.

Client-asset segregation and beneficial-ownership records matter if intermediary fails.

## 28. Legal vs Beneficial Ownership

In nominee structures, broker/custodian may hold legal title while investor is beneficial owner.

Voting, corporate actions and insolvency protections depend jurisdiction/account structure.

## 29. Brokerage Legal Entity

Global brand may serve users through different subsidiaries. Regulator, investor protection, compensation scheme and contract law may differ.

Always identify exact legal counterparty.

## 30. Omnibus vs Segregated Accounts

Omnibus custody pools client positions in intermediary account; segregated structure records more separately.

Neither label alone determines safety. Reconciliation, regulation and insolvency treatment matter.

## 31. Securities Lending

Broker/fund may lend securities. Benefits include lending revenue; risks include collateral/counterparty/recall mechanics.

Know whether opt-in/opt-out and who keeps revenue.

## 32. Operational Concentration

Holding all foreign assets, cash and FX conversion at one intermediary creates single-point failure.

Diversification of providers may improve resilience but adds complexity. Scale should justify complexity.

# Phần V — Korea và Vietnam Market Access

## 33. Korea Access

Korea offers domestic securities plus foreign-product access through brokers. Account wrappers may restrict eligible assets.

Implementation chain:

```text
Underlying
→ Wrapper
→ Account
→ Broker Entity
→ Execution
→ Tax / Reporting
```

## 34. Vietnam Access

Vietnam access may involve foreign investor registration/account/custody rules, ownership limits and specific banking/settlement processes.

Framework should treat access/repatriation as separate from security fundamentals.

## 35. Foreign Ownership Limit

Foreign room can constrain accessibility and create technical premium/discount.

Near-full room is not business moat. Regulation/issuance can change scarcity.

## 36. Free Float

Position size should be compared with **free-float market cap** and actual turnover, not total shares.

Controlling stakes reduce available liquidity and can increase governance risk.

## 37. Daily Price Limits

Vietnam price bands can make theoretical stop non-executable. Multiple floor sessions with no buyers are a real tail scenario.

Position sizing must include time-to-exit under stressed volume.

## 38. Market Impact

Cross-border investor in less-liquid market should estimate number of days needed to liquidate at reasonable participation rate.

Portfolio liquidity is not just “market is open”.

# Phần VI — Capital Mobility và Repatriation

## 39. Repatriation Risk

After selling, moving proceeds home may require banking/tax/documentation steps.

Operational friction can become country risk during stress.

## 40. Capital Controls

Country may restrict currency conversion or capital movement in exceptional conditions.

Even low-probability controls matter for assets intended to fund foreign liabilities.

## 41. Convertibility Risk

Local asset return can be high but economically less useful if proceeds cannot be converted/transferred at market rate.

Convertibility is a distinct risk from FX depreciation.

## 42. Reserve / Balance-of-Payments Context

For emerging markets, external balance, reserves and foreign-currency funding help evaluate tail capital-mobility/FX risk.

Do not use company P/E alone for cross-border allocation.

# Phần VII — Tax Framework

## 43. Tax Residency

Tax treatment depends residency and sometimes domicile/citizenship/account status.

Moving country can change reporting and wrapper suitability. Tax residency should be reviewed after major life relocation.

## 44. Source-Country Withholding

Dividend/interest may be taxed before reaching account. Treaty can modify rate or allow credits depending circumstances.

Headline dividend yield ≠ net cash yield.

## 45. Tax Treaty

Treaties coordinate taxing rights and may affect withholding/foreign-tax-credit treatment.

Treaty application can depend forms, beneficial ownership and product domicile. Verify current professional/official sources for real money.

## 46. Capital Gains

Realized gains may receive different treatment depending domestic/foreign security, account wrapper, residency and product class.

Permanent library should explain categories, not memorize one year’s rate.

## 47. Tax Wrapper

ISA/pension/retirement-like accounts can change after-tax result materially.

Evaluate contribution/withdrawal restrictions, eligible products and loss/netting rules along with tax benefit.

## 48. Tax Location

Income-heavy assets and growth assets may have different optimal account location depending jurisdiction.

The objective is maximize after-tax portfolio return, not pre-tax yield.

## 49. Foreign Tax Credit

Some systems allow credit for foreign withholding against domestic tax; rules/limits vary.

Records matter because missing statements can turn theoretical credit into unusable claim.

## 50. Estate / Inheritance Risk

Direct foreign securities may have estate/inheritance implications different from local wrappers or domiciled funds.

As portfolio grows, this deserves professional legal/tax review.

## 51. Documentation Discipline

Store trade confirmations, FX conversions, dividends, withholding statements, corporate actions, account statements and transfer records.

Cross-border tax/reporting quality depends record quality.

# Phần VIII — Cost Stack

## 52. Total Cost

```text
Broker Commission
+ Exchange / Regulatory Fees
+ Bid-Ask Spread
+ Slippage / Impact
+ FX Conversion
+ Fund Expense
+ Tracking Difference
+ Funding / Borrow
+ Tax / Withholding
+ Custody / Transfer Fees
```

“Zero commission” can still be expensive implementation.

## 53. FX Spread

Frequent currency conversion compounds friction. Compare explicit FX commission and embedded spread.

Auto-conversion of dividends can create repeated small costs.

## 54. Tracking Difference

Local wrapper may have low expense but poor tracking due tax, futures roll, hedge or operational frictions.

Historical tracking difference is often more informative than expense ratio alone.

## 55. Securities-Lending Revenue

Fund may offset fees through lending income. Analyze how much revenue returns to fund vs manager and collateral policy.

## 56. Funding Cost

Margin/CFD/leveraged products add financing. Cross-border carry can overwhelm underlying expected return over long horizon.

# Phần IX — Country, Currency và Factor Risk

## 57. Country Buckets

Classify by underlying country risk, not listing venue.

Korean-listed S&P ETF belongs mostly US/global economic bucket plus Korean wrapper operational characteristics.

## 58. Currency Buckets

Aggregate KRW/USD/VND exposures across all accounts and wrappers.

Compare net exposure with liabilities and human capital.

## 59. Factor Buckets

Countries can share factor risk. Korea semiconductor ETF, US Nasdaq and global AI fund may all long growth/tech/duration.

Country diversification is not factor diversification.

## 60. Home Bias

Familiar assets feel safer, but salary/property/pension may already concentrate domestic risk.

Foreign diversification can reduce this but adds FX/tax/access complexity. Optimal balance is household-specific.

## 61. Country Risk Premium

Political, institutional, legal and external-financing uncertainty can raise required return.

Country risk should affect valuation and position sizing, not only narrative.

## 62. Sovereign–Corporate Link

Local corporate funding cost often depends sovereign curve, banking system and currency stability.

A globally competitive company can still de-rate if country risk premium rises sharply.

## 63. Banking-System Link

Cross-border investor should assess custody/bank system stability because capital movement and corporate funding both depend financial system.

Country exposure is more than index constituents.

# Phần X — Korea–Vietnam Specific Cross-Market Thinking

## 64. Common Global Factors

Korea và Vietnam both exposed to USD, China, global trade and risk sentiment, but transmission differs.

Korea market often reprices rapidly through liquid KRW/large-cap exporters. Vietnam can transmit strongly through domestic liquidity, credit and property channels.

## 65. Fed Shock

Hawkish Fed can raise USD/yields. Korea sees KRW/foreign-flow/valuation effects; Vietnam sees VND pressure and reduced domestic easing room.

Same shock has different speed and sector weights.

## 66. China Shock

Korea has direct industrial/export links. Vietnam has trade, tourism, input and FDI-relocation channels.

China slowdown can hurt demand but lower inputs or strengthen China+1 incentives.

## 67. Oil Shock

Korea is major energy importer; Vietnam has mixed importer/producer/regulatory channels.

Company-level cost/revenue currency and pass-through determine actual outcome.

## 68. Korea Concentration

Broad Korea exposure can be semiconductor/export/industrial heavy. Adding thematic semiconductor product may duplicate risk.

## 69. Vietnam Concentration

Vietnam index can be bank/property heavy. Broad country exposure therefore still loads domestic credit/liquidity factor.

# Phần XI — Portfolio Construction

## 70. Liability-Driven Allocation

Near-term liabilities should match currency and liquidity. Money needed for Korea housing soon should not rely on VND small-cap exit or US equity recovery.

## 71. Emergency Liquidity

Cross-border transfers can fail/delay during holidays or compliance review. Keep emergency cash in readily accessible liability currency.

## 72. Cross-Border IPS

IPS should define target country/currency buckets, max FX mismatch, permitted wrappers, liquidity floor, provider concentration limits, rebalancing bands and rules for verifying policy/tax changes.

## 73. Rebalancing Across Currencies

Use new contributions/dividends where possible to rebalance without unnecessary FX conversion/tax realization.

Asset allocation rebalancing and currency rebalancing are separate decisions.

## 74. Liquidity-Adjusted Position Size

A position should be small enough to exit under stressed free-float turnover, not only normal average volume.

Estimate days-to-liquidate and price-limit risk where relevant.

## 75. Provider Concentration Limit

Large portfolio may set max exposure per broker/custodian/bank legal entity.

Operational resilience can justify holding some redundancy even if fee slightly higher.

# Phần XII — Stress Testing và Operations

## 76. Combined Stress

Test asset + FX + liquidity simultaneously:

```text
Korea equity -25%
Vietnam equity -35%
USD/KRW +15%
USD/VND +7%
Spreads double
Vietnam exits restricted by floor liquidity
Broker transfer delayed
```

Single-factor stress underestimates cross-border tails.

## 77. Reverse Stress

Ask what combination would make portfolio unable to meet 12-month liabilities or exceed target drawdown.

This identifies fragility better than only plausible scenario list.

## 78. Operational Failure

Simulate broker unavailable, bank transfer delayed, 2FA/device issue, missing tax docs or corporate-action deadline missed.

Backup access and records are portfolio infrastructure.

## 79. Succession / Access Planning

For large/long-term cross-border assets, trusted family/executor needs know where accounts and records exist, subject to security/legal safeguards.

Operational continuity matters beyond investor’s daily activity.

## 80. Snapshot Discipline

Tax, settlement, foreign-room and account rules change. Permanent docs should keep mechanisms evergreen; current decision must verify official sources dated close to transaction.

## 81. Product Comparison Template

```text
Underlying Exposure
Domicile / Legal Claim
Trading + Underlying Currency
Hedge Policy
Expense + Tracking
Spread + Liquidity
Tax / Withholding
Account Eligibility
Settlement / Market Hours
Custody / Counterparty
Estate / Reporting Complexity
```

Compare expected return after all frictions.

## 82. Pre-Trade Workflow

```text
1. Identify underlying economics.
2. Map four currencies.
3. Identify domicile/wrapper/legal claim.
4. Check liquidity/free float/price limits.
5. Check market hours/settlement/custody.
6. Estimate tax/withholding and total cost.
7. Verify repatriation/access rules.
8. Stress asset + FX + liquidity.
9. Check portfolio factor/currency duplication.
10. Size relative liabilities and liquidity.
```

## 83. Post-Trade Attribution

Separate underlying return, currency, hedge carry, income, fees, tax and execution.

Cross-border learning improves only when return source is identified correctly.

## 84. Mental Model cuối cùng

```text
Underlying Economics
→ Country / Factor Exposure
→ Currency Exposure
→ Wrapper / Domicile / Legal Claim
→ Custody / Access / Settlement
→ Tax / Cost
→ Liquidity / Repatriation
→ Liability Match
→ Stress / Operations
```

Cross-border investing is portfolio engineering across legal and monetary systems. Asset selection remains important, nhưng realized wealth depends on implementation layers that do not appear in a simple price chart.